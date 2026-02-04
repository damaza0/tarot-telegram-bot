"""
Pocket Tarot Bot
"""

import sys
import os

# Ensure project root is in Python path FIRST
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)
print(f"[BOOT] Project root: {PROJECT_ROOT}")
print(f"[BOOT] Python path: {sys.path[:3]}")

# CREATE DATABASE FIRST - before any other imports
import sqlite3

# Use /app/storage for persistent volume (NOT /app/data - that would overwrite code!)
STORAGE_DIR = "/app/storage" if os.path.exists("/app/storage") else PROJECT_ROOT
DB_FILE = os.path.join(STORAGE_DIR, "tarot_bot.db")
print(f"[BOOT] Creating database at: {DB_FILE}")

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    tokens INTEGER DEFAULT 0,
    total_tokens_earned INTEGER DEFAULT 0,
    total_tokens_spent INTEGER DEFAULT 0,
    referral_code TEXT UNIQUE,
    referred_by INTEGER,
    referral_count INTEGER DEFAULT 0,
    referral_tokens_earned INTEGER DEFAULT 0,
    last_free_reading TEXT,
    last_free_daily_reading TEXT,
    share_streak INTEGER DEFAULT 0,
    last_share_date TEXT,
    total_readings INTEGER DEFAULT 0,
    favorite_spread TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    last_active TEXT DEFAULT CURRENT_TIMESTAMP,
    is_premium INTEGER DEFAULT 0
)''')
# Add column if table already exists (migration)
try:
    c.execute('ALTER TABLE users ADD COLUMN last_free_daily_reading TEXT')
except:
    pass
c.execute('''CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    spread_type TEXT,
    cards TEXT,
    question TEXT,
    tokens_spent INTEGER DEFAULT 0,
    is_free INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)''')
c.execute('''CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    type TEXT,
    amount INTEGER,
    tokens INTEGER,
    package TEXT,
    telegram_payment_id TEXT,
    status TEXT DEFAULT 'pending',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    completed_at TEXT
)''')
c.execute('''CREATE TABLE IF NOT EXISTS referrals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    referrer_id INTEGER,
    referred_id INTEGER,
    tokens_awarded_referrer INTEGER DEFAULT 0,
    tokens_awarded_referred INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)''')
c.execute('''CREATE TABLE IF NOT EXISTS milestone_rewards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    milestone_type TEXT,
    milestone_value INTEGER,
    tokens_awarded INTEGER,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)''')
conn.commit()
conn.close()
print("[BOOT] Database tables created!")

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    PreCheckoutQueryHandler, MessageHandler, InlineQueryHandler, filters
)

import config
from utils.database import db
from handlers.readings import (
    show_reading_menu, handle_reading_callback, handle_intention_message,
    free_daily_reading, show_free_daily_status
)
from handlers.payments import (
    show_token_shop, show_free_tokens_menu,
    handle_buy_callback, precheckout_callback, successful_payment_callback
)
from handlers.referrals import (
    show_referral_menu, process_referral_start,
    show_share_prompt, handle_inline_query
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


async def delete_all_bot_messages(update: Update, context):
    """Delete ALL tracked bot messages to keep chat completely clean"""
    chat_id = update.effective_chat.id

    # Delete all tracked messages
    if 'bot_messages' in context.user_data:
        for msg_id in context.user_data['bot_messages']:
            try:
                await context.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except:
                pass  # Message may already be deleted or too old
        context.user_data['bot_messages'] = []

    # Also clean up extra_messages from readings
    if 'extra_messages' in context.user_data:
        for msg_id in context.user_data['extra_messages']:
            try:
                await context.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except:
                pass
        context.user_data['extra_messages'] = []

    # Clean up legacy tracking
    if 'last_bot_msg_id' in context.user_data:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['last_bot_msg_id'])
        except:
            pass
        context.user_data.pop('last_bot_msg_id', None)


async def delete_extra_bot_messages(update: Update, context):
    """Delete extra tracked messages but keep the current one (for button navigation)"""
    chat_id = update.effective_chat.id
    current_msg_id = update.callback_query.message.message_id if update.callback_query else None

    # Delete all tracked messages EXCEPT the current one
    if 'bot_messages' in context.user_data:
        remaining = []
        for msg_id in context.user_data['bot_messages']:
            if msg_id == current_msg_id:
                remaining.append(msg_id)
            else:
                try:
                    await context.bot.delete_message(chat_id=chat_id, message_id=msg_id)
                except:
                    pass
        context.user_data['bot_messages'] = remaining


def track_message(context, msg_id, force=False):
    """Track a bot message for later deletion"""
    # Don't track if we're in the middle of resetting (user hit /start)
    # Unless force=True (used for new menu after reset)
    if context.user_data.get('resetting') and not force:
        return
    if 'bot_messages' not in context.user_data:
        context.user_data['bot_messages'] = []
    context.user_data['bot_messages'].append(msg_id)


async def show_main_menu(update: Update, context, user_data: dict = None, force_track: bool = False):
    """Main menu"""
    user_id = update.effective_user.id

    if not user_data:
        user_data = db.get_user(user_id)

    # Defensive: make sure we have valid user data
    if not user_data:
        user_data = db.get_or_create_user(user_id, update.effective_user.username, update.effective_user.first_name)

    # Defensive: make sure tokens exists and is a number
    gems = user_data.get('tokens', 0) or 0

    # Free gem status
    can_free, seconds_until = db.can_get_free_reading(user_id)
    if can_free:
        gem_status = "🎁 *Free gem ready!*"
        gem_btn = InlineKeyboardButton("🎁 Claim Free Gem", callback_data="claim_free_gem")
    else:
        hours = seconds_until // 3600
        minutes = (seconds_until % 3600) // 60
        gem_status = f"⏳ Free gem in {hours}h {minutes}m"
        gem_btn = InlineKeyboardButton(f"⏳ Gem: {hours}h {minutes}m", callback_data="menu_free_tokens")

    # Free daily reading status
    daily_available, daily_time = await show_free_daily_status(user_id)
    if daily_available:
        daily_status = "☀️ *Free daily reading ready!*"
        daily_btn = InlineKeyboardButton("☀️ FREE Daily Reading ✨", callback_data="reading_daily_free")
    else:
        daily_status = f"☀️ Daily reading in {daily_time}"
        daily_btn = InlineKeyboardButton(f"☀️ Daily: {daily_time}", callback_data="reading_daily_free")

    menu_text = f"""🔮 *Pocket Tarot* 🔮

Hey {update.effective_user.first_name}!

💎 *{gems}* gems
{gem_status}
{daily_status}
"""

    keyboard = InlineKeyboardMarkup([
        [daily_btn],
        [gem_btn],
        [InlineKeyboardButton("🔮 Get Reading", callback_data="menu_reading")],
        [InlineKeyboardButton("💎 Gems", callback_data="menu_tokens"), InlineKeyboardButton("👥 Invite +5💎", callback_data="menu_referral")],
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(menu_text, parse_mode='Markdown', reply_markup=keyboard)
        track_message(context, update.callback_query.message.message_id, force=force_track)
    else:
        msg = await update.message.reply_text(menu_text, parse_mode='Markdown', reply_markup=keyboard)
        track_message(context, msg.message_id, force=force_track)


async def start_command(update: Update, context):
    """Handle /start"""
    try:
        user = update.effective_user
        logger.info(f"[START] User {user.id} ({user.first_name}) called /start")

        # Signal that we're resetting - stops any ongoing reading from sending more messages
        context.user_data['resetting'] = True

        # Clean up ALL old bot messages
        await delete_all_bot_messages(update, context)

        # Clear the list completely (keep resetting=True until menu is shown)
        context.user_data['bot_messages'] = []

        args = context.args

        referral_code = None
        if args and args[0].startswith('ref_'):
            referral_code = args[0][4:]
            logger.info(f"[START] User {user.id} has referral code: {referral_code}")

        user_data = await process_referral_start(
            user_id=user.id, username=user.username,
            first_name=user.first_name, referral_code=referral_code, context=context
        )
        logger.info(f"[START] User {user.id} data loaded, is_new={user_data.get('is_new', False)}")

        if user_data.get('is_new'):
            welcome_gems = user_data.get('welcome_tokens', 5)

            welcome_text = f"""🔮 *Welcome to Pocket Tarot!* 🔮

Hey {user.first_name}! You got *{welcome_gems} free gems* 💎

☀️ *FREE every day:*

• Daily tarot reading
• 1 bonus gem


🔮 *Premium readings:*

Single {config.READING_COSTS['single']}💎 · Three Card {config.READING_COSTS['three']}💎 · Relationship {config.READING_COSTS['relationship']}💎
Horseshoe {config.READING_COSTS['horseshoe']}💎 · Celtic Cross {config.READING_COSTS['celtic']}💎
"""

            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("☀️ Get Your FREE Daily Reading", callback_data="reading_daily_free")],
                [InlineKeyboardButton("🎁 Claim Free Gem", callback_data="claim_free_gem")],
                [InlineKeyboardButton("🔮 More Readings", callback_data="menu_reading")],
                [InlineKeyboardButton("👥 Invite Friends +5💎", callback_data="menu_referral")],
            ])

            msg = await update.message.reply_text(welcome_text, parse_mode='Markdown', reply_markup=keyboard)
            track_message(context, msg.message_id, force=True)
        else:
            await show_main_menu(update, context, user_data, force_track=True)

        # Now safe to allow message tracking again
        context.user_data['resetting'] = False

    except Exception as e:
        import traceback
        logger.error(f"Error in start_command for user {update.effective_user.id}: {e}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        context.user_data['resetting'] = False
        # Always send something to the user
        try:
            await update.message.reply_text(
                "🔮 *Welcome to Pocket Tarot!*\n\nSomething went wrong. Please try /start again.",
                parse_mode='Markdown'
            )
        except:
            pass


async def tokens_command(update: Update, context):
    await delete_all_bot_messages(update, context)
    await show_token_shop(update, context)

async def referral_command(update: Update, context):
    await delete_all_bot_messages(update, context)
    await show_referral_menu(update, context)

async def stats_command(update: Update, context):
    user_id = update.effective_user.id
    user = db.get_user(user_id)
    referral_stats = db.get_referral_stats(user_id)

    stats_text = f"""📊 *Your Stats*

💎 Gems: *{user['tokens']}*
🔮 Readings: *{user['total_readings']}*
👥 Referrals: *{referral_stats['total_referrals']}*
💰 Earned from refs: *{referral_stats['tokens_earned']}*💎
"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔮 Get Reading", callback_data="menu_reading")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(stats_text, parse_mode='Markdown', reply_markup=keyboard)
    else:
        await update.message.reply_text(stats_text, parse_mode='Markdown', reply_markup=keyboard)


async def help_command(update: Update, context):
    help_text = f"""🔮 *Pocket Tarot* 🔮

/start — Main menu
/gems — Buy gems
/referral — Invite friends
/stats — Your stats

☀️ *FREE every day:*
• Daily tarot reading
• 1 bonus gem

🔮 *Premium readings:*
Single {config.READING_COSTS['single']}💎 · Three Card {config.READING_COSTS['three']}💎 · Relationship {config.READING_COSTS['relationship']}💎
Horseshoe {config.READING_COSTS['horseshoe']}💎 · Celtic Cross {config.READING_COSTS['celtic']}💎

👥 Invite friends for +5💎 each!
"""

    await update.message.reply_text(help_text, parse_mode='Markdown')


async def admin_command(update: Update, context):
    """Admin command to give gems: /admin USER_ID AMOUNT"""
    user_id = update.effective_user.id

    # Check if user is admin
    if user_id != config.ADMIN_ID:
        return  # Silently ignore non-admins

    args = context.args
    if len(args) < 2:
        await update.message.reply_text(
            "*Admin Commands:*\n\n"
            "`/admin USER_ID AMOUNT` — Give gems\n"
            "`/admin me AMOUNT` — Give yourself gems\n\n"
            "Example: `/admin 123456789 500`",
            parse_mode='Markdown'
        )
        return

    # Parse user ID (allow "me" as shortcut)
    target = args[0]
    if target.lower() == "me":
        target_id = user_id
    else:
        try:
            target_id = int(target)
        except ValueError:
            await update.message.reply_text("❌ Invalid user ID")
            return

    # Parse amount
    try:
        amount = int(args[1])
    except ValueError:
        await update.message.reply_text("❌ Invalid amount")
        return

    # Add gems
    new_balance = db.add_tokens(target_id, amount)

    # Verify by reading back from database
    verified_user = db.get_user(target_id)
    verified_balance = verified_user['tokens'] if verified_user else 0

    await update.message.reply_text(
        f"✅ Gave *{amount}*💎 to user `{target_id}`\n"
        f"New balance: *{verified_balance}*💎",
        parse_mode='Markdown'
    )


async def resetuser_command(update: Update, context):
    """Admin command to reset/delete a user: /resetuser USER_ID"""
    user_id = update.effective_user.id

    # Check if user is admin
    if user_id != config.ADMIN_ID:
        return  # Silently ignore non-admins

    args = context.args
    if not args:
        await update.message.reply_text(
            "*Reset User Command:*\n\n"
            "`/resetuser USER_ID` — Delete a user so they can start fresh\n\n"
            "Example: `/resetuser 123456789`",
            parse_mode='Markdown'
        )
        return

    try:
        target_id = int(args[0])
    except ValueError:
        await update.message.reply_text("❌ Invalid user ID")
        return

    # Delete the user
    deleted = db.delete_user(target_id)

    if deleted:
        await update.message.reply_text(
            f"✅ User `{target_id}` has been deleted.\n"
            f"They will get a fresh account when they use /start",
            parse_mode='Markdown'
        )
    else:
        await update.message.reply_text(
            f"⚠️ User `{target_id}` was not found in database.",
            parse_mode='Markdown'
        )


async def handle_callback(update: Update, context):
    query = update.callback_query
    data = query.data

    user = update.effective_user
    db.get_or_create_user(user.id, user.username, user.first_name)

    if data == "menu_main":
        await query.answer()
        await delete_extra_bot_messages(update, context)
        await show_main_menu(update, context)
    elif data == "menu_reading":
        await query.answer()
        await delete_extra_bot_messages(update, context)
        await show_reading_menu(update, context)
    elif data.startswith("reading_"):
        await handle_reading_callback(update, context)
    elif data == "menu_tokens":
        await query.answer()
        await delete_extra_bot_messages(update, context)
        await show_token_shop(update, context)
    elif data == "menu_free_tokens":
        await query.answer()
        await show_free_tokens_menu(update, context)
    elif data == "claim_free_gem":
        await handle_free_gem_claim(update, context)
    elif data.startswith("buy_"):
        await handle_buy_callback(update, context)
    elif data == "menu_referral":
        await query.answer()
        await show_referral_menu(update, context)
    elif data == "menu_share":
        await query.answer()
        await show_share_prompt(update, context)
    elif data == "menu_stats":
        await query.answer()
        await stats_command(update, context)


async def handle_free_gem_claim(update: Update, context):
    """Handle free gem claim"""
    query = update.callback_query
    user_id = update.effective_user.id

    can_free, seconds_until = db.can_get_free_reading(user_id)

    if can_free:
        db.use_free_reading(user_id)
        db.add_tokens(user_id, 1)
        await query.answer("🎁 +1 gem claimed!", show_alert=True)
        await show_main_menu(update, context)
    else:
        hours = seconds_until // 3600
        minutes = (seconds_until % 3600) // 60
        await query.answer(f"⏳ Free gem in {hours}h {minutes}m", show_alert=True)


async def handle_text_message(update: Update, context):
    """Handle text messages - check for intention input"""
    # Check if user is setting an intention for a reading
    handled = await handle_intention_message(update, context)
    if handled:
        return

    # Otherwise show help hint
    await update.message.reply_text(
        "Use /start to open the menu."
    )


async def error_handler(update: Update, context):
    """Handle errors and log them"""
    logger.error(f"Error: {context.error}")

    # Try to notify user if possible
    if update and update.effective_chat:
        try:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Something went wrong. Please try /start to continue."
            )
        except:
            pass


def main():
    if config.BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("Set your bot token in config.py")
        return

    application = Application.builder().token(config.BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("gems", tokens_command))
    application.add_handler(CommandHandler("tokens", tokens_command))
    application.add_handler(CommandHandler("referral", referral_command))
    application.add_handler(CommandHandler("invite", referral_command))
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("admin", admin_command))
    application.add_handler(CommandHandler("resetuser", resetuser_command))
    application.add_handler(CallbackQueryHandler(handle_callback))
    application.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    application.add_handler(InlineQueryHandler(handle_inline_query))
    application.add_error_handler(error_handler)

    print("🔮 Pocket Tarot Bot running...")
    print(f"@{config.BOT_USERNAME}")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
