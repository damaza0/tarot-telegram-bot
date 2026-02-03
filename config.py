"""
Tarot Bot Configuration
-----------------------
Uses environment variables for sensitive data (for hosting on Railway, etc.)
"""

import os

# Telegram Bot Token (get from @BotFather)
# Set as environment variable BOT_TOKEN on Railway
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Bot username (without @)
BOT_USERNAME = os.getenv("BOT_USERNAME", "The_Arcana_Tarot_Bot")

# Database file path
DATABASE_PATH = "tarot_bot.db"

# ============== GEM PRICING ==============
# How many gems each reading costs
READING_COSTS = {
    "single": 1,        # Single card reading
    "three": 3,         # 3-card spread
    "relationship": 5,  # Relationship spread (5 cards)
    "horseshoe": 7,     # Horseshoe spread (7 cards)
    "celtic": 10,       # Celtic Cross (10 cards)
}

# Gem packages (gems, price in Telegram Stars)
# Each tier is a progressively better deal (gems per star)
TOKEN_PACKAGES = {
    "spark": {"tokens": 10, "stars": 50, "label": "✨ Spark"},         # 0.20 gems/star
    "glow": {"tokens": 30, "stars": 100, "label": "🌟 Glow"},          # 0.30 gems/star
    "shine": {"tokens": 70, "stars": 200, "label": "💫 Shine"},        # 0.35 gems/star
    "radiance": {"tokens": 130, "stars": 350, "label": "⭐ Radiance"}, # 0.37 gems/star
    "brilliance": {"tokens": 200, "stars": 500, "label": "🌙 Brilliance"}, # 0.40 gems/star
}

# ============== FREE GEM SETTINGS ==============
# Hours between free gems (20 = nearly daily)
FREE_READING_COOLDOWN_HOURS = 20

# Free gem amount per claim
FREE_GEM_AMOUNT = 1

# ============== REFERRAL SETTINGS ==============
# Gems awarded when someone uses your referral link
REFERRAL_REWARD_REFERRER = 5   # Person who shared gets 5 gems
REFERRAL_REWARD_REFERRED = 0   # New user gets nothing extra (just welcome gems)

# Welcome gems for new users
WELCOME_GEMS = 7

# Bonus gems at referral milestones
REFERRAL_MILESTONES = {
    5: 10,    # 5 referrals = 10 bonus gems
    10: 25,   # 10 referrals = 25 bonus gems
    25: 75,   # 25 referrals = 75 bonus gems
    50: 200,  # 50 referrals = 200 bonus gems
    100: 500, # 100 referrals = 500 bonus gems
}

# ============== STREAK BONUSES ==============
# Bonus gems for consecutive days of readings
STREAK_BONUSES = {
    3: 2,   # 3-day streak = 2 extra gems
    7: 5,   # 7-day streak = 5 extra gems
    14: 10, # 14-day streak = 10 extra gems
    30: 25, # 30-day streak = 25 extra gems
}

# ============== MESSAGES ==============
# Note: These templates are kept for reference but the bot uses inline text now
