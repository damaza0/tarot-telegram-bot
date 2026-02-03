# 🔮 Mystic Tarot Bot

A full-featured Telegram bot for tarot readings with a token economy, Telegram Stars payments, and viral referral system.

## Features

### 🎴 Tarot Readings
- **Single Card** (1 token) - Quick daily guidance
- **Three-Card Spread** (3 tokens) - Past, Present, Future
- **Celtic Cross** (10 cards) - Comprehensive deep reading
- Complete 78-card deck with upright and reversed meanings

### 💰 Token System
- Users purchase tokens using Telegram Stars
- Free daily single-card reading for all users
- Welcome bonus tokens for new users

### 👥 Viral Growth Features
- **Referral Program**: 5 tokens per friend invited, 3 tokens for the new user
- **Milestone Bonuses**: Extra rewards at 5, 10, 25, 50, 100 referrals
- **Daily Share Bonus**: 1 token for sharing daily
- **Streak System**: Bonus tokens for consecutive days of sharing
- **Leaderboard**: Top referrers displayed publicly
- **Inline Sharing**: Easy sharing via Telegram's inline feature

---

## Setup Instructions

### Step 1: Create Your Bot

1. Open Telegram and message [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Choose a name for your bot (e.g., "Mystic Tarot")
4. Choose a username (e.g., "MysticTarotBot") - must end in "bot"
5. **Save the API token** BotFather gives you

### Step 2: Enable Payments (Telegram Stars)

1. Still in BotFather, send `/mybots`
2. Select your bot
3. Go to **Bot Settings** → **Payments**
4. Telegram Stars is automatically available for all bots

### Step 3: Configure the Bot

1. Open `config.py`
2. Replace `YOUR_BOT_TOKEN_HERE` with your actual token:
   ```python
   BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
   ```
3. Set your bot username (without @):
   ```python
   BOT_USERNAME = "MysticTarotBot"
   ```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Bot

```bash
python bot.py
```

---

## Configuration Options

All settings are in `config.py`:

### Token Pricing
```python
READING_COSTS = {
    "single": 1,      # Single card reading
    "three": 3,       # 3-card spread
    "celtic": 10,     # Celtic Cross
}
```

### Token Packages (Telegram Stars)
```python
TOKEN_PACKAGES = {
    "starter": {"tokens": 10, "stars": 50},
    "popular": {"tokens": 25, "stars": 100},
    "premium": {"tokens": 60, "stars": 200},
    "ultimate": {"tokens": 150, "stars": 400},
}
```

### Free Reading Settings
```python
FREE_READING_COOLDOWN_HOURS = 24  # Hours between free readings
FREE_READING_TYPE = "single"      # Which reading is free
```

### Referral Rewards
```python
REFERRAL_REWARD_REFERRER = 5   # Tokens for person who shares
REFERRAL_REWARD_REFERRED = 3   # Tokens for new user

REFERRAL_MILESTONES = {
    5: 10,    # 5 referrals = 10 bonus tokens
    10: 25,   # 10 referrals = 25 bonus tokens
    25: 75,
    50: 200,
    100: 500,
}
```

### Sharing Incentives
```python
DAILY_SHARE_BONUS = 1  # Tokens per daily share

STREAK_BONUSES = {
    3: 2,    # 3-day streak = 2 extra tokens
    7: 5,
    14: 10,
    30: 25,
}
```

---

## Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot / Main menu |
| `/reading` | Get a tarot reading |
| `/tokens` | Buy tokens with Stars |
| `/referral` | Get your referral link |
| `/stats` | View your statistics |
| `/help` | Show help message |

---

## File Structure

```
tarot-telegram-bot/
├── bot.py                 # Main entry point
├── config.py              # All configuration
├── requirements.txt       # Dependencies
├── data/
│   └── tarot_cards.py     # 78 card database
├── handlers/
│   ├── readings.py        # Tarot reading logic
│   ├── payments.py        # Token purchase handling
│   └── referrals.py       # Referral & viral features
└── utils/
    └── database.py        # SQLite database manager
```

---

## Growth Strategy Tips

### Converting Free Users to Paid
1. The free daily reading creates habit and engagement
2. Three-card and Celtic Cross readings are locked behind tokens
3. Prices are set so referrals can earn enough for basic readings

### Maximizing Viral Spread
1. **Every reading ends with a share button** - make it easy
2. **Referral rewards benefit both parties** - friends get tokens too
3. **Milestone bonuses** - gamification encourages more referrals
4. **Streak system** - daily engagement through sharing rewards
5. **Leaderboard** - competitive element for top referrers

### Engagement Hooks
- 24-hour cooldown creates daily check-in habit
- Welcome bonus lets new users experience paid readings
- Referred users start with tokens, increasing retention

---

## Customization Ideas

### Add More Spreads
Edit `handlers/readings.py` to add new spread types like:
- Love reading (5 cards)
- Career reading (7 cards)
- Year ahead (12 cards)

### Custom Card Meanings
Modify `data/tarot_cards.py` to personalize the interpretations

### Different Pricing
Adjust `config.py` to experiment with:
- Different token costs
- Different package sizes
- Bigger/smaller referral rewards

---

## Support

The bot uses SQLite for data storage. The database file (`tarot_bot.db`) is created automatically on first run.

To reset all data, simply delete `tarot_bot.db`.

---

## License

Free to use and modify for your own Telegram bot projects.

🔮 May the cards guide your path! 🔮
