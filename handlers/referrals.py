"""
Referral System
"""

import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.database import db
import config


async def delete_after_delay(bot, chat_id: int, message_id: int, delay: int):
    """Delete a message after a delay"""
    await asyncio.sleep(delay)
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    except:
        pass


async def show_referral_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Referral menu"""
    user_id = update.effective_user.id
    stats = db.get_referral_stats(user_id)
    referral_link = db.get_referral_link(user_id, config.BOT_USERNAME)

    referral_text = f"""👥 *Invite Friends*

Your link:
`{referral_link}`

*Reward:* +5💎 per friend who joins

*Your stats:*
• Friends invited: *{stats['total_referrals']}*
• Gems earned: *{stats['tokens_earned']}*💎

*Milestones:*
• 5 friends — +10💎 bonus
• 10 friends — +25💎 bonus
• 25 friends — +75💎 bonus
"""

    share_msg = f"🔮 Free daily tarot readings! @{config.BOT_USERNAME}\n\n👇 Tap here to start:\n{referral_link}"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Share Link", switch_inline_query=share_msg)],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(referral_text, parse_mode='Markdown', reply_markup=keyboard)
        if 'bot_messages' not in context.user_data:
            context.user_data['bot_messages'] = []
        context.user_data['bot_messages'].append(update.callback_query.message.message_id)
    else:
        msg = await update.message.reply_text(referral_text, parse_mode='Markdown', reply_markup=keyboard)
        if 'bot_messages' not in context.user_data:
            context.user_data['bot_messages'] = []
        context.user_data['bot_messages'].append(msg.message_id)


async def process_referral_start(user_id: int, username: str, first_name: str,
                                  referral_code: str, context: ContextTypes.DEFAULT_TYPE) -> dict:
    """Process new referral"""
    user = db.get_or_create_user(
        user_id=user_id, username=username,
        first_name=first_name, referral_code=referral_code
    )

    if user.get('is_new') and user.get('referred_by'):
        referrer_id = user['referred_by']
        referrer = db.get_user(referrer_id)

        if referrer:
            referrer_stats = db.get_referral_stats(referrer_id)

            text = f"""🎉 *New Referral!*

{first_name or 'Someone'} joined using your link!

+{config.REFERRAL_REWARD_REFERRER}💎 earned
Total friends: {referrer_stats['total_referrals']}
"""

            try:
                # Send notification and auto-delete after 10 seconds
                notif_msg = await context.bot.send_message(
                    chat_id=referrer_id, text=text,
                    parse_mode='Markdown'
                )
                # Schedule deletion
                asyncio.create_task(delete_after_delay(context.bot, referrer_id, notif_msg.message_id, 10))
            except:
                pass

    return user


async def show_share_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Share prompt"""
    user_id = update.effective_user.id
    referral_link = db.get_referral_link(user_id, config.BOT_USERNAME)

    text = f"""📤 *Share Pocket Tarot*

Invite friends and earn +5💎 for each one who joins!

Your link:
`{referral_link}`
"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Share", switch_inline_query=f"🔮 Free tarot readings! @{config.BOT_USERNAME}\n\n👇 Tap here to start:\n{referral_link}")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=keyboard)
    else:
        await update.message.reply_text(text, parse_mode='Markdown', reply_markup=keyboard)


async def handle_inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inline sharing"""
    from telegram import InlineQueryResultArticle, InputTextMessageContent
    import uuid

    user_id = update.effective_user.id
    referral_link = db.get_referral_link(user_id, config.BOT_USERNAME)

    results = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="🔮 Share Pocket Tarot",
            description="Invite friends to get readings",
            input_message_content=InputTextMessageContent(
                message_text=f"🔮 *Pocket Tarot* @{config.BOT_USERNAME}\n\nGet free tarot readings every day!\n\n👇 Tap here to start:\n{referral_link}",
                parse_mode='Markdown'
            )
        )
    ]

    await update.inline_query.answer(results, cache_time=60)
