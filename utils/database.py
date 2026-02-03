"""
Database Manager for Tarot Bot
"""

import sqlite3
import os
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any, List, Tuple

import config

# Database in project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(PROJECT_ROOT, "tarot_bot.db")
print(f"[DB] Using database: {DB_PATH}")


class DatabaseManager:
    def __init__(self):
        self.db_path = DB_PATH

    def _get_conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        # Create tables if they don't exist
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT,
            tokens INTEGER DEFAULT 0, total_tokens_earned INTEGER DEFAULT 0,
            total_tokens_spent INTEGER DEFAULT 0, referral_code TEXT UNIQUE,
            referred_by INTEGER, referral_count INTEGER DEFAULT 0,
            referral_tokens_earned INTEGER DEFAULT 0, last_free_reading TEXT,
            last_free_daily_reading TEXT,
            share_streak INTEGER DEFAULT 0, last_share_date TEXT,
            total_readings INTEGER DEFAULT 0, favorite_spread TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            last_active TEXT DEFAULT CURRENT_TIMESTAMP, is_premium INTEGER DEFAULT 0
        )''')
        # Add column if table already exists (migration)
        try:
            c.execute('ALTER TABLE users ADD COLUMN last_free_daily_reading TEXT')
        except:
            pass
        c.execute('''CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
            spread_type TEXT, cards TEXT, question TEXT,
            tokens_spent INTEGER DEFAULT 0, is_free INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, type TEXT,
            amount INTEGER, tokens INTEGER, package TEXT, telegram_payment_id TEXT,
            status TEXT DEFAULT 'pending', created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            completed_at TEXT
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS referrals (
            id INTEGER PRIMARY KEY AUTOINCREMENT, referrer_id INTEGER,
            referred_id INTEGER, tokens_awarded_referrer INTEGER DEFAULT 0,
            tokens_awarded_referred INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS milestone_rewards (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
            milestone_type TEXT, milestone_value INTEGER, tokens_awarded INTEGER,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()
        return conn

    def get_or_create_user(self, user_id: int, username: str = None,
                           first_name: str = None, referral_code: str = None) -> Dict[str, Any]:
        conn = self._get_conn()
        c = conn.cursor()

        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        user = c.fetchone()

        if user:
            c.execute('''UPDATE users SET last_active = CURRENT_TIMESTAMP,
                username = COALESCE(?, username), first_name = COALESCE(?, first_name)
                WHERE user_id = ?''', (username, first_name, user_id))
            conn.commit()
            # Fetch fresh data after update
            c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            user = c.fetchone()
            conn.close()
            return dict(user)

        # New user
        import secrets
        user_ref_code = secrets.token_urlsafe(8)
        welcome = config.WELCOME_GEMS

        referred_by = None
        if referral_code:
            c.execute('SELECT user_id FROM users WHERE referral_code = ?', (referral_code,))
            ref = c.fetchone()
            if ref and ref['user_id'] != user_id:
                referred_by = ref['user_id']

        c.execute('''INSERT INTO users (user_id, username, first_name, tokens,
            total_tokens_earned, referral_code, referred_by)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (user_id, username, first_name, welcome, welcome, user_ref_code, referred_by))

        if referred_by:
            self._process_referral(c, referred_by, user_id)

        conn.commit()
        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        new_user = dict(c.fetchone())
        conn.close()

        new_user['is_new'] = True
        new_user['welcome_tokens'] = welcome
        return new_user

    def _process_referral(self, cursor, referrer_id: int, referred_id: int):
        reward = config.REFERRAL_REWARD_REFERRER

        cursor.execute('''UPDATE users SET tokens = tokens + ?,
            total_tokens_earned = total_tokens_earned + ?,
            referral_count = referral_count + 1,
            referral_tokens_earned = referral_tokens_earned + ?
            WHERE user_id = ?''', (reward, reward, reward, referrer_id))

        cursor.execute('''INSERT INTO referrals (referrer_id, referred_id,
            tokens_awarded_referrer, tokens_awarded_referred)
            VALUES (?, ?, ?, ?)''',
            (referrer_id, referred_id, reward, config.REFERRAL_REWARD_REFERRED))

        cursor.execute('SELECT referral_count FROM users WHERE user_id = ?', (referrer_id,))
        count = cursor.fetchone()['referral_count']

        if count in config.REFERRAL_MILESTONES:
            bonus = config.REFERRAL_MILESTONES[count]
            cursor.execute('''UPDATE users SET tokens = tokens + ?,
                total_tokens_earned = total_tokens_earned + ?,
                referral_tokens_earned = referral_tokens_earned + ?
                WHERE user_id = ?''', (bonus, bonus, bonus, referrer_id))

            cursor.execute('''INSERT INTO milestone_rewards
                (user_id, milestone_type, milestone_value, tokens_awarded)
                VALUES (?, 'referral', ?, ?)''', (referrer_id, count, bonus))

    def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        conn = self._get_conn()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        user = c.fetchone()
        conn.close()
        return dict(user) if user else None

    def get_user_tokens(self, user_id: int) -> int:
        user = self.get_user(user_id)
        return user['tokens'] if user else 0

    def add_tokens(self, user_id: int, amount: int, reason: str = "purchase") -> int:
        conn = self._get_conn()
        c = conn.cursor()

        # Check if user exists first
        c.execute('SELECT tokens FROM users WHERE user_id = ?', (user_id,))
        existing = c.fetchone()

        if not existing:
            # Create user with minimal data if they don't exist
            import secrets
            ref_code = secrets.token_urlsafe(8)
            c.execute('''INSERT INTO users (user_id, tokens, total_tokens_earned, referral_code)
                VALUES (?, ?, ?, ?)''', (user_id, amount, amount, ref_code))
            conn.commit()
            conn.close()
            return amount

        # User exists, update their tokens
        c.execute('''UPDATE users SET tokens = tokens + ?,
            total_tokens_earned = total_tokens_earned + ? WHERE user_id = ?''',
            (amount, amount, user_id))
        conn.commit()
        c.execute('SELECT tokens FROM users WHERE user_id = ?', (user_id,))
        balance = c.fetchone()['tokens']
        conn.close()
        return balance

    def spend_tokens(self, user_id: int, amount: int) -> tuple:
        conn = self._get_conn()
        c = conn.cursor()
        c.execute('SELECT tokens FROM users WHERE user_id = ?', (user_id,))
        current = c.fetchone()['tokens']

        if current < amount:
            conn.close()
            return False, current

        c.execute('''UPDATE users SET tokens = tokens - ?,
            total_tokens_spent = total_tokens_spent + ? WHERE user_id = ?''',
            (amount, amount, user_id))
        conn.commit()
        conn.close()
        return True, current - amount

    def can_get_free_reading(self, user_id: int) -> tuple:
        conn = self._get_conn()
        c = conn.cursor()
        c.execute('SELECT last_free_reading FROM users WHERE user_id = ?', (user_id,))
        result = c.fetchone()
        conn.close()

        if not result or not result['last_free_reading']:
            return True, None

        try:
            last = result['last_free_reading'].replace(' ', 'T')
            last_dt = datetime.fromisoformat(last)
            if last_dt.tzinfo is None:
                last_dt = last_dt.replace(tzinfo=timezone.utc)
        except:
            return True, None

        cooldown = timedelta(hours=config.FREE_READING_COOLDOWN_HOURS)
        next_avail = last_dt + cooldown
        now = datetime.now(timezone.utc)

        if now >= next_avail:
            return True, None

        secs = int((next_avail - now).total_seconds())
        return False, secs

    def use_free_reading(self, user_id: int):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute('UPDATE users SET last_free_reading = CURRENT_TIMESTAMP WHERE user_id = ?', (user_id,))
        conn.commit()
        conn.close()

    def can_get_free_daily_reading(self, user_id: int) -> tuple:
        """Check if user can claim their free daily reading"""
        conn = self._get_conn()
        c = conn.cursor()
        c.execute('SELECT last_free_daily_reading FROM users WHERE user_id = ?', (user_id,))
        result = c.fetchone()
        conn.close()

        if not result or not result['last_free_daily_reading']:
            return True, None

        try:
            last = result['last_free_daily_reading'].replace(' ', 'T')
            last_dt = datetime.fromisoformat(last)
            if last_dt.tzinfo is None:
                last_dt = last_dt.replace(tzinfo=timezone.utc)
        except:
            return True, None

        cooldown = timedelta(hours=config.FREE_READING_COOLDOWN_HOURS)
        next_avail = last_dt + cooldown
        now = datetime.now(timezone.utc)

        if now >= next_avail:
            return True, None

        secs = int((next_avail - now).total_seconds())
        return False, secs

    def use_free_daily_reading(self, user_id: int):
        """Mark free daily reading as used, starting cooldown"""
        conn = self._get_conn()
        c = conn.cursor()
        c.execute('UPDATE users SET last_free_daily_reading = ? WHERE user_id = ?',
                  (datetime.now(timezone.utc).isoformat(), user_id))
        conn.commit()
        conn.close()

    def record_reading(self, user_id: int, spread_type: str, cards: str,
                       question: str = None, tokens_spent: int = 0, is_free: bool = False):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute('''INSERT INTO readings (user_id, spread_type, cards, question, tokens_spent, is_free)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (user_id, spread_type, cards, question, tokens_spent, 1 if is_free else 0))
        c.execute('UPDATE users SET total_readings = total_readings + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        conn.close()

    def get_referral_stats(self, user_id: int) -> Dict[str, Any]:
        conn = self._get_conn()
        c = conn.cursor()
        c.execute('SELECT referral_code, referral_count, referral_tokens_earned FROM users WHERE user_id = ?', (user_id,))
        user = c.fetchone()
        conn.close()

        if not user:
            return {'referral_code': '', 'total_referrals': 0, 'tokens_earned': 0}

        return {
            'referral_code': user['referral_code'],
            'total_referrals': user['referral_count'],
            'tokens_earned': user['referral_tokens_earned']
        }

    def get_referral_link(self, user_id: int, bot_username: str) -> str:
        user = self.get_user(user_id)
        return f"https://t.me/{bot_username}?start=ref_{user['referral_code']}"

    def create_transaction(self, user_id: int, package: str, telegram_payment_id: str = None) -> int:
        pkg = config.TOKEN_PACKAGES.get(package)
        if not pkg:
            return None

        conn = self._get_conn()
        c = conn.cursor()
        c.execute('''INSERT INTO transactions (user_id, type, amount, tokens, package, telegram_payment_id, status, completed_at)
            VALUES (?, 'purchase', ?, ?, ?, ?, 'completed', CURRENT_TIMESTAMP)''',
            (user_id, pkg['stars'], pkg['tokens'], package, telegram_payment_id))
        tid = c.lastrowid
        conn.commit()
        conn.close()
        return tid

    def get_top_referrers(self, limit: int = 10) -> List[Dict[str, Any]]:
        conn = self._get_conn()
        c = conn.cursor()
        c.execute('''SELECT user_id, first_name, username, referral_count, referral_tokens_earned
            FROM users WHERE referral_count > 0 ORDER BY referral_count DESC LIMIT ?''', (limit,))
        leaders = [dict(row) for row in c.fetchall()]
        conn.close()
        return leaders


# Create instance
db = DatabaseManager()
