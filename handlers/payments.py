"""
Gem Shop & Payments
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
from telegram.ext import ContextTypes
from utils.database import db
import config


def track_msg(context, msg_id):
    """Track a message for later deletion (respects resetting flag)"""
    if context.user_data.get('resetting'):
        return
    if 'bot_messages' not in context.user_data:
        context.user_data['bot_messages'] = []
    context.user_data['bot_messages'].append(msg_id)


async def show_token_shop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gem shop"""
    user_id = update.effective_user.id
    user = db.get_user(user_id)
    gems = user['tokens'] if user else 0

    shop_text = f"""💎 *Gem Shop*

Balance: *{gems}*💎

*Packages:*
• Spark — 10💎 for 50⭐
• Glow — 30💎 for 100⭐
• Shine — 70💎 for 200⭐
• Radiance — 130💎 for 350⭐
• Brilliance — 200💎 for 500⭐

_Payment via Telegram Stars_
"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✨ Spark 10💎 — 50⭐", callback_data="buy_spark")],
        [InlineKeyboardButton("🌟 Glow 30💎 — 100⭐", callback_data="buy_glow")],
        [InlineKeyboardButton("💫 Shine 70💎 — 200⭐", callback_data="buy_shine")],
        [InlineKeyboardButton("⭐ Radiance 130💎 — 350⭐", callback_data="buy_radiance")],
        [InlineKeyboardButton("🌙 Brilliance 200💎 — 500⭐", callback_data="buy_brilliance")],
        [InlineKeyboardButton("🎁 Free Gems", callback_data="menu_free_tokens")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(shop_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, update.callback_query.message.message_id)
    else:
        msg = await update.message.reply_text(shop_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, msg.message_id)


async def show_free_tokens_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Free gems info"""
    user_id = update.effective_user.id
    referral_stats = db.get_referral_stats(user_id)

    can_free, seconds_until = db.can_get_free_reading(user_id)

    if can_free:
        free_status = "🎁 Free gem available now!"
        free_btn = InlineKeyboardButton("🎁 Claim Free Gem", callback_data="claim_free_gem")
    else:
        hours = seconds_until // 3600
        minutes = (seconds_until % 3600) // 60
        free_status = f"⏳ Free gem in {hours}h {minutes}m"
        free_btn = InlineKeyboardButton(f"⏳ {hours}h {minutes}m", callback_data="claim_free_gem")

    free_text = f"""🎁 *Free Gems*

{free_status}

*Daily:*
• 1 free gem every 20 hours

*Referrals:*
• +5💎 per friend you invite

Your referrals: *{referral_stats['total_referrals']}*
Earned: *{referral_stats['tokens_earned']}*💎
"""

    keyboard = InlineKeyboardMarkup([
        [free_btn],
        [InlineKeyboardButton("👥 Invite Friends +5💎", callback_data="menu_referral")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(free_text, parse_mode='Markdown', reply_markup=keyboard)
    else:
        await update.message.reply_text(free_text, parse_mode='Markdown', reply_markup=keyboard)


async def handle_buy_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle purchase"""
    query = update.callback_query
    await query.answer()

    package_key = query.data.replace("buy_", "")

    if package_key not in config.TOKEN_PACKAGES:
        await query.answer("Invalid package!", show_alert=True)
        return

    package = config.TOKEN_PACKAGES[package_key]

    title = f"{package['tokens']} Gems"
    description = f"Get {package['tokens']} gems for tarot readings"
    prices = [LabeledPrice(label=title, amount=package['stars'])]

    try:
        # Delete the shop menu before sending invoice
        try:
            await query.message.delete()
        except:
            pass

        invoice_msg = await context.bot.send_invoice(
            chat_id=update.effective_chat.id,
            title=title,
            description=description,
            payload=f"gems_{package_key}_{update.effective_user.id}",
            provider_token="",  # Empty for Telegram Stars
            currency="XTR",
            prices=prices
        )
        # Track invoice message for cleanup
        track_msg(context, invoice_msg.message_id)

        # Send a cancel option below the invoice
        cancel_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("❌ Cancel", callback_data="menu_tokens")]
        ])
        cancel_msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="_Tap above to pay, or cancel below_",
            parse_mode='Markdown',
            reply_markup=cancel_keyboard
        )
        track_msg(context, cancel_msg.message_id)

    except Exception as e:
        print(f"Payment error: {e}")  # Log the actual error
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back to Shop", callback_data="menu_tokens")],
            [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
        ])
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"❌ *Could not create payment*\n\nError: {str(e)[:100]}",
            parse_mode='Markdown',
            reply_markup=keyboard
        )
        track_msg(context, msg.message_id)


async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Validate payment"""
    query = update.pre_checkout_query
    try:
        parts = query.invoice_payload.split("_")
        if parts[0] == "gems" and parts[1] in config.TOKEN_PACKAGES:
            await query.answer(ok=True)
        else:
            await query.answer(ok=False, error_message="Invalid purchase")
    except:
        await query.answer(ok=False, error_message="Something went wrong")


async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle successful payment"""
    payment = update.message.successful_payment
    user_id = update.effective_user.id

    # Delete all tracked messages (including invoice)
    chat_id = update.effective_chat.id
    if 'bot_messages' in context.user_data:
        for msg_id in context.user_data['bot_messages']:
            try:
                await context.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except:
                pass
        context.user_data['bot_messages'] = []

    parts = payment.invoice_payload.split("_")
    package_key = parts[1]
    package = config.TOKEN_PACKAGES[package_key]

    new_balance = db.add_tokens(user_id, package['tokens'], reason="purchase")

    db.create_transaction(
        user_id=user_id,
        package=package_key,
        telegram_payment_id=payment.telegram_payment_charge_id
    )

    success_text = f"""✅ *Payment Successful!*

+{package['tokens']}💎 added
New balance: *{new_balance}*💎
"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔮 Get Reading", callback_data="menu_reading")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    msg = await update.message.reply_text(success_text, parse_mode='Markdown', reply_markup=keyboard)
    track_msg(context, msg.message_id)
