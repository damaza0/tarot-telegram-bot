"""
Daily Advice Messages for Free Daily Reading
Each card has specific guidance for the person's day
"""

DAILY_ADVICE = {
    # === MAJOR ARCANA ===
    "The Fool": {
        "emoji": "🃏",
        "upright": "Today invites you to take a leap of faith! Say yes to something unexpected. Don't overthink - trust your instincts and embrace spontaneity. A fresh start or new opportunity may present itself. Be open to adventure, even small ones.",
        "reversed": "Pause before making any impulsive decisions today. That exciting opportunity might need more consideration. It's okay to slow down and think things through. Ground yourself before taking action."
    },
    "The Magician": {
        "emoji": "🎩",
        "upright": "You have everything you need to make things happen today! Take initiative on that project or conversation you've been putting off. Your words and actions carry extra power - use them wisely. Manifest your intentions.",
        "reversed": "Double-check your work today - details might slip through. Be wary of miscommunication or promises that seem too good. Focus on one thing at a time rather than juggling too much."
    },
    "The High Priestess": {
        "emoji": "🌙",
        "upright": "Trust your gut feelings today - they're spot on. Pay attention to dreams, hunches, and subtle signs. Take some quiet time for yourself if possible. The answers you seek are already within you.",
        "reversed": "You might be ignoring an important inner voice today. Stop second-guessing yourself. If something feels off, don't dismiss it. Reconnect with your intuition through stillness."
    },
    "The Empress": {
        "emoji": "👑",
        "upright": "Nurture yourself and others today. Beauty, comfort, and creative expression are favored. Treat yourself to something that delights your senses. Your caring energy will be appreciated by those around you.",
        "reversed": "Watch for neglecting your own needs while caring for others. Self-care isn't selfish - it's necessary. If creativity feels blocked, don't force it. Rest and replenish first."
    },
    "The Emperor": {
        "emoji": "🏛️",
        "upright": "Take charge of your day with structure and confidence. Set clear boundaries and stick to your plans. Leadership opportunities may arise - step up. Organization and discipline will serve you well.",
        "reversed": "Flexibility is key today. Don't be too rigid with yourself or others. If you're feeling controlling or controlled, step back. Find balance between structure and flow."
    },
    "The Hierophant": {
        "emoji": "📿",
        "upright": "Seek wisdom from trusted sources today - a mentor, teacher, or tradition. Following established procedures will serve you well. It's a good day for learning and honoring your values.",
        "reversed": "Question the rules today. What traditions or expectations no longer serve you? Think for yourself rather than just following the crowd. Your unique perspective matters."
    },
    "The Lovers": {
        "emoji": "💕",
        "upright": "Meaningful connections are highlighted today. Have that heart-to-heart conversation. Make choices aligned with your values. Love and harmony flow when you're authentic.",
        "reversed": "Check in with yourself before making relationship decisions today. Are you being true to yourself? Address any inner conflict about what you really want. Self-love comes first."
    },
    "The Chariot": {
        "emoji": "🏆",
        "upright": "Victory is within reach - push forward with determination! Stay focused on your goal and don't let distractions derail you. Confidence and willpower will carry you through any obstacles today.",
        "reversed": "Feeling pulled in different directions? Pause and regain your focus before charging ahead. Forcing things won't work today - find your center first. Control what you can, release what you can't."
    },
    "Strength": {
        "emoji": "🦁",
        "upright": "Approach today's challenges with patience and compassion rather than force. Your inner strength is your superpower. Gentle persistence wins. You're more resilient than you know.",
        "reversed": "Be extra kind to yourself today - self-doubt may creep in. You don't have to be tough all the time. It's okay to admit you're struggling and ask for support."
    },
    "The Hermit": {
        "emoji": "🏔️",
        "upright": "Solitude and reflection serve you well today. Take time away from the noise to think things through. The answers come from within, not from others. Trust your own wisdom.",
        "reversed": "Don't isolate too much today - connection is needed. Reach out to someone you trust. Avoiding problems won't make them disappear. Balance alone time with meaningful interaction."
    },
    "Wheel of Fortune": {
        "emoji": "🎡",
        "upright": "Luck is on your side today! Be open to unexpected opportunities and positive changes. Go with the flow of life's cycles. A turning point may be at hand.",
        "reversed": "If things feel stuck or unlucky, remember this is temporary. Look for the lesson in the challenge. Don't resist change - work with it. Better times are coming."
    },
    "Justice": {
        "emoji": "⚖️",
        "upright": "Fairness and truth prevail today. Take responsibility for your choices. Legal or official matters are favored. Make decisions based on facts and ethics, not emotions.",
        "reversed": "Something may feel unfair today. Before reacting, examine all sides honestly. Are you being fully accountable? Seek truth even if it's uncomfortable."
    },
    "The Hanged Man": {
        "emoji": "🙃",
        "upright": "Pause and look at things from a completely different angle today. Waiting or delays may actually be helpful. Surrender the need to control everything. Fresh perspective comes from stillness.",
        "reversed": "Stop stalling on that decision you've been avoiding. Waiting isn't helping anymore - it's time to act or let go. Break free from the mental loop."
    },
    "Death": {
        "emoji": "🦋",
        "upright": "Let go of what's no longer serving you today. An ending makes space for a beautiful new beginning. Transformation is natural - don't cling to the old. Embrace change.",
        "reversed": "You may be resisting a necessary ending. What are you holding onto out of fear? Release and trust that something better awaits. Change is inevitable."
    },
    "Temperance": {
        "emoji": "⚗️",
        "upright": "Balance and moderation are your allies today. Don't rush - patience brings better results. Blend different aspects of your life harmoniously. Find the middle path.",
        "reversed": "Life may feel out of balance today. Check for excess in some area - too much work, too little rest? Realign your priorities. Healing comes through balance."
    },
    "The Devil": {
        "emoji": "⛓️",
        "upright": "Examine what's keeping you stuck today. Unhealthy patterns, habits, or attachments? You have more power to break free than you realize. Face your shadow honestly.",
        "reversed": "You're breaking free from something that held you back! Continue releasing old patterns. Liberation is happening. Stay aware and don't slip back."
    },
    "The Tower": {
        "emoji": "⚡",
        "upright": "Expect the unexpected today. A sudden change or revelation may shake things up, but it clears the way for something better. Embrace the breakthrough, however uncomfortable.",
        "reversed": "You sense change coming but are resisting it. The longer you hold on to unstable structures, the harder the fall. Let go before you're forced to."
    },
    "The Star": {
        "emoji": "⭐",
        "upright": "Hope and healing shine on you today! Your wishes can manifest. Have faith and stay optimistic. Share your light with others. Inspiration flows freely.",
        "reversed": "If hope feels dim today, look for small moments of beauty. Your light is still there, just temporarily clouded. Reconnect with what inspires you. Faith will return."
    },
    "The Moon": {
        "emoji": "🌕",
        "upright": "Trust your intuition today, especially if things seem unclear. Pay attention to dreams and hunches. Not everything is as it appears - look beneath the surface. Navigate by your inner light.",
        "reversed": "Confusion clears today. Fears that seemed huge may shrink in daylight. Hidden truths emerge. Trust that clarity is coming."
    },
    "The Sun": {
        "emoji": "☀️",
        "upright": "Joy and success light up your day! Everything feels brighter and more possible. Celebrate the good things, big and small. Share your happiness - it multiplies when given away.",
        "reversed": "Your inner sunshine may feel dimmed today. Don't let temporary clouds block your joy. Reconnect with simple pleasures and your inner child. The sun is still there."
    },
    "Judgement": {
        "emoji": "📯",
        "upright": "A moment of reckoning or important decision arrives today. Listen to your higher calling. Forgive yourself and others. Rise to your true purpose.",
        "reversed": "Don't ignore that inner voice calling you to something more. Self-judgment may be too harsh - ease up. What's your soul really asking for?"
    },
    "The World": {
        "emoji": "🌍",
        "upright": "Completion and achievement mark your day! Celebrate how far you've come. A cycle ends successfully. The whole world opens with new possibilities.",
        "reversed": "So close to the finish line - don't give up now! Completion is within reach but may need a bit more effort. Tie up loose ends. Closure comes soon."
    },

    # === WANDS ===
    "Ace of Wands": {
        "emoji": "🪄",
        "upright": "A spark of inspiration hits today! Act on that creative idea or new opportunity. Your enthusiasm is contagious. Start something new while the energy is high.",
        "reversed": "Feeling uninspired or blocked? Don't force creativity. The spark will return. Focus on clearing obstacles first."
    },
    "Two of Wands": {
        "emoji": "🗺️",
        "upright": "Plan your next move today. Think big about future possibilities. Decisions about direction need to be made. The world is open to you.",
        "reversed": "Fear of the unknown may be holding you back. Don't let comfort zones limit your vision. Take a small step toward something bigger."
    },
    "Three of Wands": {
        "emoji": "🚢",
        "upright": "Your efforts begin paying off today. Expansion is favored. Look toward the horizon for opportunities. Progress is happening, even if you can't see the full picture yet.",
        "reversed": "Delays may frustrate you, but don't abandon your plans. Reassess and adjust rather than giving up. Patience with long-term goals."
    },
    "Four of Wands": {
        "emoji": "🎊",
        "upright": "Celebrate today! A milestone, gathering, or moment of harmony deserves recognition. Home and family matters are blessed. Enjoy the stability you've created.",
        "reversed": "Home or community may feel unsettled. Work on creating inner harmony first. Celebration can wait until foundations are solid."
    },
    "Five of Wands": {
        "emoji": "⚔️",
        "upright": "Expect some competition or conflicting opinions today. Stand your ground but stay respectful. Challenges strengthen you. Channel competitive energy constructively.",
        "reversed": "Avoid unnecessary conflicts today. Pick your battles wisely. Finding common ground serves everyone better than fighting."
    },
    "Six of Wands": {
        "emoji": "🏅",
        "upright": "Victory and recognition come your way today! Accept praise graciously. Your confidence inspires others. Lead by example.",
        "reversed": "Don't rely on external validation today. Success may be private rather than public. Find confidence within yourself."
    },
    "Seven of Wands": {
        "emoji": "🛡️",
        "upright": "Defend your position today. Others may challenge you, but you're in a strong spot. Don't back down from what you believe in. Persevere.",
        "reversed": "You may be exhausted from defending yourself. Is this battle worth fighting? Sometimes stepping back is the wisest move."
    },
    "Eight of Wands": {
        "emoji": "✈️",
        "upright": "Things move fast today! Swift developments, quick messages, rapid progress. Strike while momentum is on your side. Action, action, action!",
        "reversed": "Frustrating delays may slow you down. Use this time to prepare. When things speed up again, you'll be ready."
    },
    "Nine of Wands": {
        "emoji": "💪",
        "upright": "You're almost there - one more push! Don't give up now. Draw on your reserves of strength. You've survived worse and you'll make it through this.",
        "reversed": "Burnout warning. You've been fighting too long. Rest before you collapse. It's okay to ask for help or take a break."
    },
    "Ten of Wands": {
        "emoji": "😓",
        "upright": "Heavy burdens today. You may be carrying too much. Prioritize ruthlessly and delegate what you can. Success shouldn't crush you.",
        "reversed": "Time to release some responsibilities. You don't have to do everything yourself. Drop what's not essential before it drops you."
    },
    "Page of Wands": {
        "emoji": "🌱",
        "upright": "Explore something new today! Fresh ideas and enthusiasm spark curiosity. Be a beginner at something. News about a creative venture may arrive.",
        "reversed": "Don't let fear of failure stop you from starting. Scattered energy needs focusing. What excites you most? Start there."
    },
    "Knight of Wands": {
        "emoji": "🐎",
        "upright": "Charge forward with passion today! Be bold and adventurous. Take action on what fires you up. Just don't be reckless.",
        "reversed": "Slow down before you crash. Impulsive moves backfire today. Channel that fiery energy more carefully."
    },
    "Queen of Wands": {
        "emoji": "🔥",
        "upright": "Own your confidence today! Be warm, bold, and magnetic. Your charisma attracts opportunities. Lead with passion and inspire others.",
        "reversed": "Confidence may waver today. Don't let jealousy (yours or others') dim your flame. Reconnect with what makes you powerful."
    },
    "King of Wands": {
        "emoji": "👑",
        "upright": "Lead with vision and integrity today. Others look to you for direction. Be the inspiring leader - bold but honorable. Big picture thinking favored.",
        "reversed": "Check your ego today. Leadership without listening becomes tyranny. Are you being too controlling or impulsive?"
    },

    # === CUPS ===
    "Ace of Cups": {
        "emoji": "💝",
        "upright": "Your heart opens wide today! Love, compassion, and emotional fulfillment flow. Express your feelings. New relationships or deeper connections are blessed.",
        "reversed": "Emotional blocks may need clearing. Fill your own cup first before giving to others. Self-love is the foundation."
    },
    "Two of Cups": {
        "emoji": "💑",
        "upright": "Beautiful connection today! Partnership, romance, or deep friendship flourishes. Meet someone halfway. Mutual respect and love are highlighted.",
        "reversed": "Relationship imbalance needs addressing. Are you giving too much or too little? Focus on self-love before partnership."
    },
    "Three of Cups": {
        "emoji": "🥂",
        "upright": "Celebrate with friends today! Social gatherings, collaboration, and shared joy are favored. Community lifts you up. Say yes to invitations.",
        "reversed": "Social energy may feel draining. It's okay to skip the gathering. Watch for gossip or overindulgence."
    },
    "Four of Cups": {
        "emoji": "😔",
        "upright": "Look around with fresh eyes today - you might be missing an opportunity right in front of you. Boredom or dissatisfaction signals it's time to shift perspective.",
        "reversed": "You're waking up to new possibilities! Grab that opportunity you've been ignoring. Motivation returns."
    },
    "Five of Cups": {
        "emoji": "😢",
        "upright": "If you're feeling loss or disappointment today, let yourself grieve - but don't miss what remains. Not all is lost. Hope persists.",
        "reversed": "Healing begins. You're starting to move forward from loss. Accept the past and embrace what's still standing."
    },
    "Six of Cups": {
        "emoji": "🧸",
        "upright": "Nostalgia and sweet memories warm your heart today. Reconnect with your inner child or someone from your past. Innocent joy is available.",
        "reversed": "Don't get stuck living in the past. Nostalgia is nice to visit but not to live in. Move forward with the lessons learned."
    },
    "Seven of Cups": {
        "emoji": "💭",
        "upright": "Many options appear today, but not all are realistic. Daydreaming is fine, but ground your choices in reality. Discern illusion from opportunity.",
        "reversed": "Clarity cuts through confusion. You know what really matters now. Make choices based on values, not fantasy."
    },
    "Eight of Cups": {
        "emoji": "🚶",
        "upright": "It may be time to walk away from something unfulfilling today. Leaving takes courage. Trust that something better awaits on a new path.",
        "reversed": "Fear keeps you stuck in an unsatisfying situation. Find the courage to leave, or make peace with staying. No more limbo."
    },
    "Nine of Cups": {
        "emoji": "😊",
        "upright": "Wishes come true today! Contentment and satisfaction fill your heart. Enjoy this blessed time. Gratitude multiplies joy.",
        "reversed": "External achievements feel empty? True happiness comes from within. What really fulfills you beyond surface things?"
    },
    "Ten of Cups": {
        "emoji": "🌈",
        "upright": "Emotional fulfillment and harmony bless your day! Family and relationships flourish. This is the happily-ever-after energy. Savor it.",
        "reversed": "Perfect pictures have cracks. Work on authentic harmony rather than appearances. What does your heart really need?"
    },
    "Page of Cups": {
        "emoji": "🐟",
        "upright": "Sweet messages of love or creativity arrive today. Follow your intuition and inner child. Be open to emotional surprises.",
        "reversed": "Don't let insecurity silence your creativity or feelings. Emotional immaturity may need addressing. Trust your sensitive side."
    },
    "Knight of Cups": {
        "emoji": "🦢",
        "upright": "Follow your heart today! Romantic gestures, creative pursuits, and emotional adventures call. Lead with love and imagination.",
        "reversed": "Romantic idealism may lead to disappointment. Ground your feelings in reality. Watch for moodiness."
    },
    "Queen of Cups": {
        "emoji": "🌊",
        "upright": "Be the calm in the storm today. Your emotional wisdom and compassion help others. Trust your deep intuition. Nurture with love.",
        "reversed": "Your giving nature may be depleted. Take care of yourself first. Watch for absorbing others' emotions or codependency."
    },
    "King of Cups": {
        "emoji": "🔱",
        "upright": "Balance emotion with wisdom today. Stay calm and compassionate even in difficult situations. Your steady presence helps everyone.",
        "reversed": "Emotions may be suppressed or overwhelming. Find healthy ways to express what you feel. Don't let feelings control you."
    },

    # === SWORDS ===
    "Ace of Swords": {
        "emoji": "⚔️",
        "upright": "Mental clarity breaks through today! Truth cuts through confusion. New ideas and intellectual victories emerge. Speak and think with precision.",
        "reversed": "Mental fog may cloud your thinking. Don't make major decisions until clarity returns. The truth may be hard to face."
    },
    "Two of Swords": {
        "emoji": "🤔",
        "upright": "A difficult decision faces you today. Weigh options carefully but don't avoid choosing forever. Remove the blindfold and see clearly.",
        "reversed": "Information overload paralyzes you. Trust your gut and choose. Analysis paralysis helps no one."
    },
    "Three of Swords": {
        "emoji": "💔",
        "upright": "Heartache may touch today, but painful truths heal better than comfortable lies. Feel your feelings fully. Healing begins with acknowledgment.",
        "reversed": "Healing from hurt begins today. The worst is passing. Forgiveness (of self or others) releases the pain."
    },
    "Four of Swords": {
        "emoji": "😴",
        "upright": "Rest is essential today! Step back from the noise. Mental burnout requires stillness. Recharge through quiet time.",
        "reversed": "You're not resting enough - or finally starting to recover. Either way, prioritize restoration. Continued stress leads to breakdown."
    },
    "Five of Swords": {
        "emoji": "😤",
        "upright": "Not every battle is worth winning today. A hollow victory costs too much. Consider if the fight matters or if it's time to walk away.",
        "reversed": "Time to end conflicts and move forward. Seek reconciliation where possible. Holding grudges hurts you most."
    },
    "Six of Swords": {
        "emoji": "⛵",
        "upright": "You're moving toward calmer waters today. Leave troubles behind. The transition may be difficult but leads somewhere better.",
        "reversed": "Emotional baggage weighs down your journey. Release it before moving on. What do you need to let go of?"
    },
    "Seven of Swords": {
        "emoji": "🥷",
        "upright": "Be strategic today, but stay honest. Watch for deception - from others or the temptation in yourself. Not everything is as it appears.",
        "reversed": "Secrets want to come out. It's better to confess than be caught. Come clean and face the music."
    },
    "Eight of Swords": {
        "emoji": "🏚️",
        "upright": "Feeling trapped? The prison is mostly in your mind today. You have more options than you think. Look for the way out - it exists.",
        "reversed": "Breaking free from mental limitations! You're seeing that escape was always possible. Liberation comes through changed thinking."
    },
    "Nine of Swords": {
        "emoji": "😰",
        "upright": "Anxiety may keep you up today. Your worries likely seem worse than reality. Talk to someone, get perspective, and be gentle with yourself.",
        "reversed": "Anxiety begins to lift. Face your fears in daylight - they shrink. Support is available. Reach out."
    },
    "Ten of Swords": {
        "emoji": "😵",
        "upright": "Rock bottom, but also the turning point. The worst is over. This painful ending makes way for new beginnings. Dawn follows darkness.",
        "reversed": "Recovery begins from difficulty. You're rising again. Or - stop prolonging an inevitable ending. Let it be done."
    },
    "Page of Swords": {
        "emoji": "🔍",
        "upright": "Curiosity drives you today! Seek information, learn something new, communicate your ideas. Mental energy is high - channel it well.",
        "reversed": "Think before speaking today. Sharp words cut. Gossip or hasty messages cause problems. Pause before hitting send."
    },
    "Knight of Swords": {
        "emoji": "🌪️",
        "upright": "Charge forward with determination today! Quick thinking and decisive action are favored. Just don't run over others in your rush.",
        "reversed": "Slow down before you crash. Reckless mental energy scatters effectiveness. Think before charging ahead."
    },
    "Queen of Swords": {
        "emoji": "👸",
        "upright": "Be clear-headed and direct today. Set boundaries with compassion. Your honest communication cuts through confusion. Discernment is your power.",
        "reversed": "Sharp intellect may turn cutting. Watch for being overly critical - of yourself or others. Balance head with heart."
    },
    "King of Swords": {
        "emoji": "⚖️",
        "upright": "Lead with clear thinking and ethics today. Your intellect serves truth and justice. Make decisions from wisdom, not emotion.",
        "reversed": "Mental power without compassion becomes cold. Are you being too harsh or manipulative? Balance authority with empathy."
    },

    # === PENTACLES ===
    "Ace of Pentacles": {
        "emoji": "💰",
        "upright": "A golden opportunity for material or financial gain appears today! New income, career prospects, or investments are blessed. Plant seeds of abundance.",
        "reversed": "A financial opportunity may slip away or scarcity thinking blocks abundance. Ground yourself and stay practical."
    },
    "Two of Pentacles": {
        "emoji": "🤹",
        "upright": "Juggle your responsibilities with grace today. Balance is key - work, money, life. Stay adaptable and flexible.",
        "reversed": "Too many balls in the air? Something needs to drop before you do. Prioritize ruthlessly and ask for help."
    },
    "Three of Pentacles": {
        "emoji": "🏗️",
        "upright": "Teamwork succeeds today! Collaborate with others on practical projects. Your skills are valued. Build something together.",
        "reversed": "Team friction or working alone when collaboration would help. Address communication issues. Don't try to do everything yourself."
    },
    "Four of Pentacles": {
        "emoji": "🏦",
        "upright": "Protect your resources today, but don't hoard out of fear. Financial security through smart saving. Balance holding on and letting flow.",
        "reversed": "Loosen your grip on money or control. Generosity or necessary spending is called for. Trust the flow."
    },
    "Five of Pentacles": {
        "emoji": "🥶",
        "upright": "If you're feeling lack or left out today, remember: help is available if you look for it. Don't let pride keep you from support.",
        "reversed": "Financial or material recovery begins. The worst passes. Accept help offered. Things improve."
    },
    "Six of Pentacles": {
        "emoji": "🎁",
        "upright": "Generosity flows both ways today. Give what you can and receive graciously. Balance in exchange. Share your abundance.",
        "reversed": "Watch for strings attached to giving or receiving. Power imbalance in exchanges? Seek genuine generosity."
    },
    "Seven of Pentacles": {
        "emoji": "🌱",
        "upright": "Patience with your investments today - growth takes time. Assess progress but don't pull up roots to check. Keep tending your garden.",
        "reversed": "Frustrated with slow results? Reassess whether this investment is worth continuing. Some seeds won't grow no matter what."
    },
    "Eight of Pentacles": {
        "emoji": "🔨",
        "upright": "Focus on skill-building and quality work today. Diligent effort pays off. Practice makes progress. Mastery comes through dedication.",
        "reversed": "Work feels uninspiring or perfectionism blocks completion. Reconnect with purpose. Done is better than perfect."
    },
    "Nine of Pentacles": {
        "emoji": "🍇",
        "upright": "Enjoy the fruits of your labor today! Financial independence and comfort are yours to savor. Treat yourself - you've earned it.",
        "reversed": "Material success feels empty? True abundance includes more than money. What non-material riches do you crave?"
    },
    "Ten of Pentacles": {
        "emoji": "🏰",
        "upright": "Long-term security and family prosperity are highlighted today. Think about legacy and lasting wealth. Stability supports those you love.",
        "reversed": "Family or financial matters may be complicated. Don't sacrifice relationships for money. Address inheritance or shared resource issues."
    },
    "Page of Pentacles": {
        "emoji": "📚",
        "upright": "A practical opportunity for learning or earning appears today. Stay grounded while pursuing goals. Study something useful.",
        "reversed": "Practical goals stall or learning feels pointless. Don't let fear stop you from starting. Take one small real-world step."
    },
    "Knight of Pentacles": {
        "emoji": "🐢",
        "upright": "Slow and steady wins today. Hard work and routine build lasting results. Be dependable and persistent. Patience pays.",
        "reversed": "Routine becomes rut or motivation slumps. Shake things up. What's one small change that brings fresh energy?"
    },
    "Queen of Pentacles": {
        "emoji": "🌻",
        "upright": "Create comfort and security today through practical nurturing. Care for yourself and others in tangible ways. Abundance flows through your hands.",
        "reversed": "Are you neglecting yourself while providing for others? Balance nurturing with self-care. You can't pour from empty."
    },
    "King of Pentacles": {
        "emoji": "💎",
        "upright": "Master material matters with wisdom today. Business decisions are sound. Your practical leadership creates lasting security.",
        "reversed": "Money obsession or financial instability need addressing. Don't sacrifice what really matters for wealth. Reassess priorities."
    }
}

def get_daily_advice(card_name: str, reversed: bool = False) -> dict:
    """Get daily advice for a specific card"""
    if card_name not in DAILY_ADVICE:
        return None

    card = DAILY_ADVICE[card_name]
    orientation = "reversed" if reversed else "upright"

    return {
        "name": card_name,
        "emoji": card["emoji"],
        "reversed": reversed,
        "advice": card[orientation]
    }
