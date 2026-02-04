"""
Tarot Reading Handlers
"""

import random
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.tarot_cards import get_all_cards
from data.daily_advice import get_daily_advice, DAILY_ADVICE
from utils.database import db
import config


def track_msg(context, msg_id):
    """Track a message for later deletion (respects resetting flag)"""
    if context.user_data.get('resetting'):
        return  # Don't track during reset
    if 'bot_messages' not in context.user_data:
        context.user_data['bot_messages'] = []
    context.user_data['bot_messages'].append(msg_id)


def draw_cards(count: int) -> list:
    """Draw random cards"""
    all_cards = get_all_cards()
    drawn = random.sample(all_cards, count)
    return [{'card': card, 'reversed': random.random() < 0.5} for card in drawn]


def convert_to_past_tense(text):
    """Convert present tense text to past tense"""
    replacements = [
        ("You have", "You had"),
        ("you have", "you had"),
        ("You are", "You were"),
        ("you are", "you were"),
        ("You're", "You were"),
        ("you're", "you were"),
        ("is being", "was being"),
        ("are being", "were being"),
        ("This is", "This was"),
        ("this is", "this was"),
        ("It's", "It was"),
        ("it's", "it was"),
        ("awaits", "awaited"),
        ("approaches", "approached"),
        ("emerges", "emerged"),
        ("reveals", "revealed"),
        ("shows", "showed"),
        ("brings", "brought"),
        ("comes", "came"),
        ("needs", "needed"),
        ("requires", "required"),
        ("suggests", "suggested"),
        ("indicates", "indicated"),
        ("means", "meant"),
        ("calls", "called"),
        ("asks", "asked"),
        ("wants", "wanted"),
        ("seeks", "sought"),
        ("finds", "found"),
        ("feels", "felt"),
        ("seems", "seemed"),
        ("appears", "appeared"),
        ("exists", "existed"),
        ("flows", "flowed"),
        ("shines", "shone"),
        ("burns", "burned"),
        ("grows", "grew"),
        ("rises", "rose"),
        ("falls", "fell"),
        ("stands", "stood"),
        ("lies", "lay"),
        ("holds", "held"),
        ("takes", "took"),
        ("makes", "made"),
        ("gives", "gave"),
        ("leads", "led"),
        ("speaks", "spoke"),
        ("tells", "told"),
        ("opens", "opened"),
        ("closes", "closed"),
        ("begins", "began"),
        ("ends", "ended"),
        ("continues", "continued"),
        ("remains", "remained"),
        ("stays", "stayed"),
        ("moves", "moved"),
        ("changes", "changed"),
        ("transforms", "transformed"),
        (" is ", " was "),
        (" are ", " were "),
        ("can ", "could "),
        ("will ", "would "),
        ("may ", "might "),
    ]
    result = text
    for old, new in replacements:
        result = result.replace(old, new)
    return result


def convert_to_future_tense(text):
    """Convert present tense text to future tense"""
    replacements = [
        ("You have", "You will have"),
        ("you have", "you will have"),
        ("You are", "You will be"),
        ("you are", "you will be"),
        ("You're", "You will be"),
        ("you're", "you will be"),
        ("This is", "This will be"),
        ("this is", "this will be"),
        ("It's", "It will be"),
        ("it's", "it will be"),
        ("awaits", "will await"),
        ("approaches", "will approach"),
        ("emerges", "will emerge"),
        ("reveals", "will reveal"),
        ("shows", "will show"),
        ("brings", "will bring"),
        ("comes", "will come"),
        ("needs", "will need"),
        ("requires", "will require"),
        ("suggests", "will suggest"),
        ("indicates", "will indicate"),
        ("means", "will mean"),
        ("calls", "will call"),
        ("asks", "will ask"),
        ("wants", "will want"),
        ("seeks", "will seek"),
        ("finds", "will find"),
        ("feels", "will feel"),
        ("seems", "will seem"),
        ("appears", "will appear"),
        ("exists", "will exist"),
        ("flows", "will flow"),
        ("shines", "will shine"),
        ("burns", "will burn"),
        ("grows", "will grow"),
        ("rises", "will rise"),
        ("falls", "will fall"),
        ("stands", "will stand"),
        ("lies", "will lie"),
        ("holds", "will hold"),
        ("takes", "will take"),
        ("makes", "will make"),
        ("gives", "will give"),
        ("leads", "will lead"),
        ("speaks", "will speak"),
        ("tells", "will tell"),
        ("opens", "will open"),
        ("closes", "will close"),
        ("begins", "will begin"),
        ("ends", "will end"),
        ("continues", "will continue"),
        ("remains", "will remain"),
        ("stays", "will stay"),
        ("moves", "will move"),
        ("changes", "will change"),
        ("transforms", "will transform"),
        (" is ", " will be "),
        (" are ", " will be "),
        ("can ", "will be able to "),
    ]
    result = text
    for old, new in replacements:
        result = result.replace(old, new)
    return result


def get_card_summary(card_data: dict) -> str:
    """Get a brief summary of a card for sharing"""
    card = card_data['card']
    is_reversed = card_data['reversed']
    orientation = "reversed" if is_reversed else "upright"
    keywords = card[orientation]['keywords'][:2]
    rev = " ʀᴇᴠ" if is_reversed else ""
    return f"{card['emoji']} {card['name']}{rev} ({', '.join(keywords)})"


def get_brief_keywords(card_data: dict, count: int = 2) -> str:
    """Get brief keywords from a card"""
    card = card_data['card']
    orientation = "reversed" if card_data['reversed'] else "upright"
    return ", ".join(card[orientation]['keywords'][:count])


def format_card(card_data: dict, position: str = None, description: str = None, tense: str = "present") -> str:
    """Format a card for display"""
    card = card_data['card']
    is_reversed = card_data['reversed']
    rev = " (Reversed) 🔄" if is_reversed else ""
    orientation = "reversed" if is_reversed else "upright"

    keywords = card[orientation]['keywords'][:4]
    keywords_text = " • ".join(keywords)

    text = ""
    if position:
        if description:
            text += f"*{position.upper()}* — _{description}_\n\n"
        else:
            text += f"*{position.upper()}*\n\n"
    text += f"{card['emoji']} *{card['name']}{rev}*\n\n"
    text += f"*{keywords_text}*"

    return text


async def single_card_reading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Single card reading"""
    user_id = update.effective_user.id
    cards = draw_cards(1)
    card_data = cards[0]
    card = card_data['card']

    reading_text = f"""🔮 *Single Card Reading*

_A single card offers a focused message, one energy or theme to reflect on._

{format_card(card_data)}
"""

    db.record_reading(
        user_id=user_id, spread_type="single",
        cards=json.dumps([{'name': card['name'], 'reversed': card_data['reversed']}]),
        tokens_spent=config.READING_COSTS['single'], is_free=False
    )

    referral_link = db.get_referral_link(user_id, config.BOT_USERNAME)
    rev_label = " (Reversed)" if card_data['reversed'] else ""
    keywords = get_brief_keywords(card_data, 2)
    share_text = f"🔮 I drew {card['emoji']} {card['name']}{rev_label}!\n\n✨ {keywords}\n\n👇 Try it yourself:\n{referral_link}"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Share", switch_inline_query=share_text)],
        [InlineKeyboardButton("🔮 Another Reading", callback_data="menu_reading")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, update.callback_query.message.message_id)
    else:
        msg = await update.effective_message.reply_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, msg.message_id)


async def three_card_reading(update: Update, context: ContextTypes.DEFAULT_TYPE, intention: str = None):
    """Three card spread with tense-appropriate descriptions"""
    user_id = update.effective_user.id
    cards = draw_cards(3)

    # Position: (name, description, tense)
    positions = [
        ("Past", "the energy that has settled or the foundation that was built", "past"),
        ("Present", "the current energy that bridges the past and future", "present"),
        ("Future", "the energy that awaits on the current path", "future")
    ]

    reading_text = "🎴 *Three Card Spread*\n\n"
    reading_text += "_This spread reveals how a situation has developed, where it stands now, and where it may be heading._\n\n"
    if intention:
        reading_text += f"_Focus: {intention}_\n\n"

    cards_data = []
    for i, (pos_name, desc, tense) in enumerate(positions):
        card_data = cards[i]
        cards_data.append({'name': card_data['card']['name'], 'reversed': card_data['reversed']})
        reading_text += f"{format_card(card_data, pos_name, desc, tense)}\n\n"

    db.record_reading(
        user_id=user_id, spread_type="three",
        cards=json.dumps(cards_data),
        tokens_spent=config.READING_COSTS['three'], is_free=False
    )

    referral_link = db.get_referral_link(user_id, config.BOT_USERNAME)
    # Build brief summary of the 3 cards
    past_card = cards[0]['card']
    present_card = cards[1]['card']
    future_card = cards[2]['card']
    share_text = (
        f"🎴 My 3-Card Reading:\n"
        f"Past: {past_card['emoji']} {past_card['name']}\n"
        f"Present: {present_card['emoji']} {present_card['name']}\n"
        f"Future: {future_card['emoji']} {future_card['name']}\n\n"
        f"👇 Try it yourself:\n{referral_link}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Share", switch_inline_query=share_text)],
        [InlineKeyboardButton("🔮 Another Reading", callback_data="menu_reading")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, update.callback_query.message.message_id)
    else:
        msg = await update.effective_message.reply_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, msg.message_id)


async def celtic_cross_reading(update: Update, context: ContextTypes.DEFAULT_TYPE, intention: str = None):
    """Celtic Cross (10 cards) - all in one message"""
    user_id = update.effective_user.id
    cards = draw_cards(10)

    # Position: (name, description, tense)
    positions = [
        ("The Present", "core of situation or current state", "present"),
        ("The Challenge", "energy that demands attention", "present"),
        ("The Root", "foundation that was built or the origin", "past"),
        ("The Recent Past", "energy that is leaving or settling", "past"),
        ("The Crown", "highest potential or best outcome", "future"),
        ("The Near Future", "what energy is around the corner", "future"),
        ("The Self", "self image, attitude or true inner thoughts and feelings", "present"),
        ("The Environment", "outside world influence or perception", "present"),
        ("Hopes and Fears", "hopes and/or fears", "present"),
        ("The Outcome", "long term result, where this is leading", "future")
    ]

    # Build the full reading
    reading_text = "🌙 *Celtic Cross Reading*\n\n"
    if intention:
        reading_text += f"_Focus: {intention}_\n\n"

    cards_data = []
    for i, (pos_name, desc, tense) in enumerate(positions):
        card_data = cards[i]
        cards_data.append({'name': card_data['card']['name'], 'reversed': card_data['reversed']})
        reading_text += f"{format_card(card_data, pos_name, desc, tense)}"
        if i < 9:
            reading_text += "\n\n---\n\n"

    db.record_reading(
        user_id=user_id, spread_type="celtic",
        cards=json.dumps(cards_data),
        question=intention,
        tokens_spent=config.READING_COSTS['celtic'], is_free=False
    )

    outcome = cards[9]
    outcome_card = outcome['card']
    outcome_keywords = get_brief_keywords(outcome, 2)
    outcome_rev = " (Reversed)" if outcome['reversed'] else ""

    present = cards[0]['card']
    referral_link = db.get_referral_link(user_id, config.BOT_USERNAME)
    share_text = (
        f"🌙 My Celtic Cross Reading:\n"
        f"Present: {present['emoji']} {present['name']}\n"
        f"Outcome: {outcome_card['emoji']} {outcome_card['name']}{outcome_rev}\n"
        f"✨ {outcome_keywords}\n\n"
        f"👇 Try it yourself:\n{referral_link}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Share", switch_inline_query=share_text)],
        [InlineKeyboardButton("🔮 Another Reading", callback_data="menu_reading")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, update.callback_query.message.message_id)
    else:
        msg = await update.effective_message.reply_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, msg.message_id)


async def relationship_reading(update: Update, context: ContextTypes.DEFAULT_TYPE, intention: str = None):
    """Relationship spread (5 cards)"""
    user_id = update.effective_user.id
    cards = draw_cards(5)

    # Position: (name, description, tense)
    # Using neutral terms so reading can be about any two people
    positions = [
        ("First Person", "energy representing one side of the connection", "present"),
        ("Second Person", "energy representing the other side", "present"),
        ("The Bond", "the shared foundation or dynamic of the relationship", "present"),
        ("The Challenge", "the energy causing tension or obstacles", "present"),
        ("The Advice", "energy to be aware of, a remedy to the challenge", "future")
    ]

    intro = "💕 *Relationship Reading*\n\n"
    intro += "_This spread explores the dynamics between two people: what each brings, what connects them, and what challenges they face._\n\n"
    if intention:
        intro += f"_Focus: {intention}_\n\n"

    reading_text = intro

    cards_data = []
    for i, (pos_name, desc, tense) in enumerate(positions):
        card_data = cards[i]
        cards_data.append({'name': card_data['card']['name'], 'reversed': card_data['reversed']})
        reading_text += f"{format_card(card_data, pos_name, desc, tense)}"
        if i < len(positions) - 1:
            reading_text += "\n\n---\n\n"

    db.record_reading(
        user_id=user_id, spread_type="relationship",
        cards=json.dumps(cards_data),
        question=intention,
        tokens_spent=config.READING_COSTS['relationship'], is_free=False
    )

    bond_card = cards[2]['card']
    advice_card = cards[4]['card']
    referral_link = db.get_referral_link(user_id, config.BOT_USERNAME)
    share_text = (
        f"💕 My Relationship Reading:\n"
        f"The Bond: {bond_card['emoji']} {bond_card['name']}\n"
        f"Advice: {advice_card['emoji']} {advice_card['name']}\n\n"
        f"👇 Try it yourself:\n{referral_link}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Share", switch_inline_query=share_text)],
        [InlineKeyboardButton("🔮 Another Reading", callback_data="menu_reading")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, update.callback_query.message.message_id)
    else:
        msg = await update.effective_message.reply_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, msg.message_id)


async def horseshoe_reading(update: Update, context: ContextTypes.DEFAULT_TYPE, intention: str = None):
    """Horseshoe spread (7 cards)"""
    user_id = update.effective_user.id
    cards = draw_cards(7)

    # Position: (name, description, tense)
    positions = [
        ("Past", "the energy that has settled or the foundation that was built", "past"),
        ("Present", "the current energy or state", "present"),
        ("Hidden Influences", "forces at work beneath the surface", "present"),
        ("Obstacles", "energy that hinders progress", "present"),
        ("External Forces", "people or circumstances affecting things", "present"),
        ("Advice", "energy to be aware of, a remedy to the obstacle", "future"),
        ("Outcome", "where things are likely heading", "future")
    ]

    intro = "🧲 *Horseshoe Reading*\n\n"
    intro += "_This spread uncovers hidden influences, obstacles, and guidance, offering a clear path from past to potential outcome._\n\n"
    if intention:
        intro += f"_Your focus: {intention}_\n\n"

    reading_text = intro

    cards_data = []
    for i, (pos_name, desc, tense) in enumerate(positions):
        card_data = cards[i]
        cards_data.append({'name': card_data['card']['name'], 'reversed': card_data['reversed']})
        reading_text += f"{format_card(card_data, pos_name, desc, tense)}"
        if i < len(positions) - 1:
            reading_text += "\n\n---\n\n"

    db.record_reading(
        user_id=user_id, spread_type="horseshoe",
        cards=json.dumps(cards_data),
        question=intention,
        tokens_spent=config.READING_COSTS['horseshoe'], is_free=False
    )

    outcome = cards[6]
    outcome_card = outcome['card']
    outcome_keywords = get_brief_keywords(outcome, 2)
    outcome_rev = " (Reversed)" if outcome['reversed'] else ""
    present = cards[1]['card']

    referral_link = db.get_referral_link(user_id, config.BOT_USERNAME)
    share_text = (
        f"🧲 My Horseshoe Reading:\n"
        f"Present: {present['emoji']} {present['name']}\n"
        f"Outcome: {outcome_card['emoji']} {outcome_card['name']}{outcome_rev}\n"
        f"✨ {outcome_keywords}\n\n"
        f"👇 Try it yourself:\n{referral_link}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Share", switch_inline_query=share_text)],
        [InlineKeyboardButton("🔮 Another Reading", callback_data="menu_reading")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, update.callback_query.message.message_id)
    else:
        msg = await update.effective_message.reply_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, msg.message_id)


async def show_intention_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE, reading_type: str):
    """Show intention setting prompt before deep readings"""

    if reading_type == "three":
        prompt_text = """🎴 *Three Card Spread*

Past · Present · Future

*What situation would you like insight on?*

Type your focus below, or tap Skip for a general reading.

_Examples:_
_• "My career over the next few months"_
_• "How this relationship is evolving"_
_• "Where I am with my personal goals"_
"""
    elif reading_type == "celtic":
        prompt_text = """🌙 *Celtic Cross Reading*

Before we begin, take a moment to set your intention.

*What situation or question would you like guidance on?*

Type your intention below, or tap Skip for a general reading.

_Examples:_
_• "My career path"_
_• "Should I move forward with this decision?"_
_• "What do I need to know about my living situation?"_
"""
    elif reading_type == "horseshoe":
        prompt_text = """🧲 *Horseshoe Reading*

Before we begin, focus on what you'd like clarity on.

*What question or situation would you like guidance on?*

Type your focus below, or tap Skip for a general reading.

_Examples:_
_• "My current job situation"_
_• "A decision I'm facing"_
_• "What I need to know about this opportunity"_
"""
    else:  # relationship
        prompt_text = """💕 *Relationship Reading*

Before we begin, focus on the connection you want to explore.

*Who or what relationship is this reading about?*

Type your focus below, or tap Skip for a general reading.

_Examples:_
_• "My relationship with Alex"_
_• "A new connection I'm forming"_
_• "The dynamic between my parents"_
"""

    # Store the reading type they selected
    context.user_data['awaiting_intention'] = reading_type

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⏭️ Skip — General Reading", callback_data=f"reading_{reading_type}_skip")],
        [InlineKeyboardButton("🔙 Back", callback_data="menu_reading")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(prompt_text, parse_mode='Markdown', reply_markup=keyboard)
        # Track this message so we can delete it when user types their intention
        context.user_data['intention_prompt_msg_id'] = update.callback_query.message.message_id
    else:
        await update.message.reply_text(prompt_text, parse_mode='Markdown', reply_markup=keyboard)


async def show_reading_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Reading selection menu"""
    user_id = update.effective_user.id

    # Clear intention state
    context.user_data.pop('intention_prompt_msg_id', None)
    context.user_data.pop('awaiting_intention', None)

    user = db.get_user(user_id)
    gems = user['tokens'] if user else 0

    # Check free daily reading status
    daily_available, daily_status = await show_free_daily_status(user_id)

    if daily_available:
        daily_btn_text = "☀️ FREE Daily Reading ✨"
        daily_line = "• *FREE Daily Reading* — Available now!"
    else:
        daily_btn_text = f"☀️ Daily Reading — {daily_status}"
        daily_line = f"• *FREE Daily Reading* — {daily_status}"

    menu_text = f"""🔮 *Choose Reading*

💎 *{gems}* gems

{daily_line}

• *Single Card* — {config.READING_COSTS['single']}💎
• *Three Card* — {config.READING_COSTS['three']}💎
• *Relationship* — {config.READING_COSTS['relationship']}💎
• *Horseshoe* — {config.READING_COSTS['horseshoe']}💎
• *Celtic Cross* — {config.READING_COSTS['celtic']}💎
"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(daily_btn_text, callback_data="reading_daily_free")],
        [InlineKeyboardButton(f"🃏 Single — {config.READING_COSTS['single']}💎", callback_data="reading_single")],
        [InlineKeyboardButton(f"🎴 Three Card — {config.READING_COSTS['three']}💎", callback_data="reading_three")],
        [InlineKeyboardButton(f"💕 Relationship — {config.READING_COSTS['relationship']}💎", callback_data="reading_relationship")],
        [InlineKeyboardButton(f"🧲 Horseshoe — {config.READING_COSTS['horseshoe']}💎", callback_data="reading_horseshoe")],
        [InlineKeyboardButton(f"🌙 Celtic Cross — {config.READING_COSTS['celtic']}💎", callback_data="reading_celtic")],
        [InlineKeyboardButton("💎 Get Gems", callback_data="menu_tokens")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(menu_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, update.callback_query.message.message_id)
    else:
        msg = await update.message.reply_text(menu_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, msg.message_id)


async def handle_reading_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle reading callbacks"""
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    data = query.data

    # Simple readings (no intention needed)
    simple_costs = {
        "reading_single": ("single", config.READING_COSTS['single']),
    }

    # Readings that need intention prompt first
    intention_costs = {
        "reading_three": ("three", config.READING_COSTS['three']),
        "reading_celtic": ("celtic", config.READING_COSTS['celtic']),
        "reading_horseshoe": ("horseshoe", config.READING_COSTS['horseshoe']),
        "reading_relationship": ("relationship", config.READING_COSTS['relationship']),
    }

    # Skip intention (general reading)
    skip_costs = {
        "reading_three_skip": ("three", config.READING_COSTS['three']),
        "reading_celtic_skip": ("celtic", config.READING_COSTS['celtic']),
        "reading_horseshoe_skip": ("horseshoe", config.READING_COSTS['horseshoe']),
        "reading_relationship_skip": ("relationship", config.READING_COSTS['relationship']),
    }

    # Free daily reading
    if data == "reading_daily_free":
        await free_daily_reading(update, context)
        return

    if data in simple_costs:
        reading_type, cost = simple_costs[data]
        success, balance = db.spend_tokens(user_id, cost)

        if not success:
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 Get Gems", callback_data="menu_tokens")],
                [InlineKeyboardButton("🔙 Back", callback_data="menu_reading")]
            ])
            await query.edit_message_text(
                f"❌ Not enough gems!\n\nNeed *{cost}*💎, you have *{balance}*💎",
                parse_mode='Markdown', reply_markup=keyboard
            )
            return

        if reading_type == "single":
            await single_card_reading(update, context)

    elif data in intention_costs:
        reading_type, cost = intention_costs[data]
        balance = db.get_user_tokens(user_id)

        if balance < cost:
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 Get Gems", callback_data="menu_tokens")],
                [InlineKeyboardButton("🔙 Back", callback_data="menu_reading")]
            ])
            await query.edit_message_text(
                f"❌ Not enough gems!\n\nNeed *{cost}*💎, you have *{balance}*💎",
                parse_mode='Markdown', reply_markup=keyboard
            )
            return

        # Show intention prompt
        await show_intention_prompt(update, context, reading_type)

    elif data in skip_costs:
        reading_type, cost = skip_costs[data]
        success, balance = db.spend_tokens(user_id, cost)

        if not success:
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 Get Gems", callback_data="menu_tokens")],
                [InlineKeyboardButton("🔙 Back", callback_data="menu_reading")]
            ])
            await query.edit_message_text(
                f"❌ Not enough gems!\n\nNeed *{cost}*💎, you have *{balance}*💎",
                parse_mode='Markdown', reply_markup=keyboard
            )
            return

        # Clear intention state
        context.user_data.pop('awaiting_intention', None)
        context.user_data.pop('intention_prompt_msg_id', None)

        if reading_type == "three":
            await three_card_reading(update, context, intention=None)
        elif reading_type == "celtic":
            await celtic_cross_reading(update, context, intention=None)
        elif reading_type == "horseshoe":
            await horseshoe_reading(update, context, intention=None)
        elif reading_type == "relationship":
            await relationship_reading(update, context, intention=None)


async def handle_intention_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user's typed intention for deep readings"""
    if 'awaiting_intention' not in context.user_data:
        return False

    reading_type = context.user_data.pop('awaiting_intention')
    intention = update.message.text.strip()
    user_id = update.effective_user.id

    # Delete the intention prompt message
    if 'intention_prompt_msg_id' in context.user_data:
        try:
            await context.bot.delete_message(
                chat_id=update.effective_chat.id,
                message_id=context.user_data.pop('intention_prompt_msg_id')
            )
        except:
            pass

    cost = config.READING_COSTS[reading_type]
    success, balance = db.spend_tokens(user_id, cost)

    if not success:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💎 Get Gems", callback_data="menu_tokens")],
            [InlineKeyboardButton("🔙 Back", callback_data="menu_reading")]
        ])
        await update.message.reply_text(
            f"❌ Not enough gems!\n\nNeed *{cost}*💎, you have *{balance}*💎",
            parse_mode='Markdown', reply_markup=keyboard
        )
        return True

    if reading_type == "three":
        await three_card_reading(update, context, intention=intention)
    elif reading_type == "celtic":
        await celtic_cross_reading(update, context, intention=intention)
    elif reading_type == "horseshoe":
        await horseshoe_reading(update, context, intention=intention)
    elif reading_type == "relationship":
        await relationship_reading(update, context, intention=intention)

    return True


async def free_daily_reading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Free daily reading with specific daily advice"""
    user_id = update.effective_user.id
    user = db.get_user(user_id)

    if not user:
        await update.effective_message.reply_text("Please /start first!")
        return

    # Check cooldown
    can_claim, seconds_left = db.can_get_free_daily_reading(user_id)

    if not can_claim:
        hours = seconds_left // 3600
        mins = (seconds_left % 3600) // 60
        time_str = f"{hours}h {mins}m" if hours else f"{mins}m"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔮 Paid Readings", callback_data="menu_reading")],
            [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
        ])

        cooldown_text = (
            f"⏳ *Daily Reading Cooldown*\n\n"
            f"Your next free reading is available in *{time_str}*\n\n"
            f"_Want a reading now? Try our paid options!_"
        )

        if update.callback_query:
            await update.callback_query.edit_message_text(cooldown_text, parse_mode='Markdown', reply_markup=keyboard)
        else:
            await update.effective_message.reply_text(cooldown_text, parse_mode='Markdown', reply_markup=keyboard)
        return

    # Draw a single card
    cards = draw_cards(1)
    card_data = cards[0]
    card = card_data['card']
    is_reversed = card_data['reversed']

    # Get daily advice
    advice_data = get_daily_advice(card['name'], is_reversed)

    if advice_data:
        advice = advice_data['advice']
    else:
        # Fallback if card not in daily advice
        advice = "Take this card's energy with you today and see how it manifests."

    rev_text = " (Reversed) 🔄" if is_reversed else ""
    orientation = "reversed" if is_reversed else "upright"
    keywords = card[orientation]['keywords'][:3]
    keywords_text = " • ".join(keywords)

    reading_text = f"""☀️ *Your Daily Reading*

_A single card to set the tone for the day, a theme to carry forward._

{card['emoji']} *{card['name']}*{rev_text}

*{keywords_text}*

---

*Today's Message:*
{advice}
"""

    # Mark as claimed - starts the cooldown
    db.use_free_daily_reading(user_id)

    # Record the reading
    db.record_reading(
        user_id=user_id,
        spread_type="daily_free",
        cards=json.dumps([{'name': card['name'], 'reversed': is_reversed}]),
        tokens_spent=0,
        is_free=True
    )

    referral_link = db.get_referral_link(user_id, config.BOT_USERNAME)
    rev_share = " (Reversed)" if is_reversed else ""
    share_keywords = ", ".join(keywords[:2])
    share_text = (
        f"☀️ My daily card: {card['emoji']} {card['name']}{rev_share}\n"
        f"✨ {share_keywords}\n\n"
        f"👇 Get your free daily reading:\n{referral_link}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Share", switch_inline_query=share_text)],
        [InlineKeyboardButton("🔮 More Readings", callback_data="menu_reading")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu_main")]
    ])

    if update.callback_query:
        await update.callback_query.edit_message_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, update.callback_query.message.message_id)
    else:
        msg = await update.effective_message.reply_text(reading_text, parse_mode='Markdown', reply_markup=keyboard)
        track_msg(context, msg.message_id)


async def show_free_daily_status(user_id: int) -> tuple:
    """Check free daily reading status and return (available, time_str)"""
    can_claim, seconds_left = db.can_get_free_daily_reading(user_id)

    if can_claim:
        return True, "Ready!"
    else:
        hours = seconds_left // 3600
        mins = (seconds_left % 3600) // 60
        time_str = f"{hours}h {mins}m" if hours else f"{mins}m"
        return False, time_str
