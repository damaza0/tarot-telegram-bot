"""
Complete Tarot Card Database
78 cards with meanings for upright and reversed positions
"""

MAJOR_ARCANA = [
    {
        "name": "The Fool",
        "number": 0,
        "emoji": "🃏",
        "upright": {
            "keywords": ["new beginnings", "innocence", "spontaneity", "free spirit"],
            "meaning": "A new chapter awaits you. Embrace the unknown with an open heart and trust in the journey ahead. This is a time for taking leaps of faith and starting fresh adventures."
        },
        "reversed": {
            "keywords": ["recklessness", "risk-taking", "holding back", "fear"],
            "meaning": "You may be holding back from a new opportunity due to fear, or perhaps rushing into something without thinking. Find balance between caution and courage."
        }
    },
    {
        "name": "The Magician",
        "number": 1,
        "emoji": "🎩",
        "upright": {
            "keywords": ["manifestation", "resourcefulness", "power", "inspired action"],
            "meaning": "You have all the tools and resources you need to manifest your desires. Channel your willpower and focus your intentions. The universe supports your creative endeavors."
        },
        "reversed": {
            "keywords": ["manipulation", "poor planning", "untapped talents", "deception"],
            "meaning": "Be wary of manipulation or trickery, either from others or within yourself. You may not be using your full potential. Realign with your authentic power."
        }
    },
    {
        "name": "The High Priestess",
        "number": 2,
        "emoji": "🌙",
        "upright": {
            "keywords": ["intuition", "sacred knowledge", "divine feminine", "subconscious"],
            "meaning": "Trust your inner voice and pay attention to your dreams. Hidden knowledge is being revealed to you. This is a time for introspection and connecting with your deeper wisdom."
        },
        "reversed": {
            "keywords": ["secrets", "disconnection", "withdrawal", "silence"],
            "meaning": "You may be ignoring your intuition or keeping secrets that need to be revealed. Reconnect with your inner guidance and trust what you already know."
        }
    },
    {
        "name": "The Empress",
        "number": 3,
        "emoji": "👑",
        "upright": {
            "keywords": ["femininity", "beauty", "nature", "nurturing", "abundance"],
            "meaning": "Abundance flows to you now. Nurture yourself and others. Creative projects flourish. Connect with nature and embrace the sensual pleasures of life."
        },
        "reversed": {
            "keywords": ["creative block", "dependence", "emptiness", "neglect"],
            "meaning": "You may be neglecting self-care or feeling creatively blocked. Reconnect with what nourishes your soul and address any codependent patterns."
        }
    },
    {
        "name": "The Emperor",
        "number": 4,
        "emoji": "🏛️",
        "upright": {
            "keywords": ["authority", "structure", "control", "fatherhood", "stability"],
            "meaning": "Take charge of your situation with confidence and authority. Create structure and order in your life. Leadership opportunities arise. Stand firm in your boundaries."
        },
        "reversed": {
            "keywords": ["tyranny", "rigidity", "coldness", "excess"],
            "meaning": "Watch for controlling behavior in yourself or others. Flexibility is needed. Too much rigidity blocks growth. Find balance between structure and flow."
        }
    },
    {
        "name": "The Hierophant",
        "number": 5,
        "emoji": "📿",
        "upright": {
            "keywords": ["spiritual wisdom", "tradition", "conformity", "morality", "ethics"],
            "meaning": "Seek guidance from spiritual teachers or traditional wisdom. This is a time for learning and following established paths. Honor your beliefs and values."
        },
        "reversed": {
            "keywords": ["personal beliefs", "freedom", "challenging status quo", "rebellion"],
            "meaning": "Question traditions that no longer serve you. Your own inner wisdom may conflict with conventional beliefs. Find your unique spiritual path."
        }
    },
    {
        "name": "The Lovers",
        "number": 6,
        "emoji": "💕",
        "upright": {
            "keywords": ["love", "harmony", "relationships", "values alignment", "choices"],
            "meaning": "A meaningful connection or important choice awaits. Align with your heart's true desires. Relationships deepen through honest communication and shared values."
        },
        "reversed": {
            "keywords": ["self-love", "disharmony", "imbalance", "misalignment"],
            "meaning": "Relationship challenges or internal conflict about values. Focus on self-love first. Ensure your choices align with your authentic self."
        }
    },
    {
        "name": "The Chariot",
        "number": 7,
        "emoji": "🏆",
        "upright": {
            "keywords": ["control", "willpower", "success", "action", "determination"],
            "meaning": "Victory through determination! Take the reins and drive forward with confidence. You have the willpower to overcome obstacles. Success is within reach."
        },
        "reversed": {
            "keywords": ["self-discipline", "opposition", "lack of direction", "aggression"],
            "meaning": "You may feel pulled in different directions or out of control. Regain focus and discipline. Avoid forcing situations - find your center first."
        }
    },
    {
        "name": "Strength",
        "number": 8,
        "emoji": "🦁",
        "upright": {
            "keywords": ["strength", "courage", "patience", "influence", "compassion"],
            "meaning": "True strength comes from within. Approach challenges with patience and compassion rather than force. You have the inner courage to face any situation."
        },
        "reversed": {
            "keywords": ["inner strength", "self-doubt", "weakness", "insecurity"],
            "meaning": "Self-doubt may be undermining your confidence. Remember your inner power. This is a call to develop self-compassion and reclaim your courage."
        }
    },
    {
        "name": "The Hermit",
        "number": 9,
        "emoji": "🏔️",
        "upright": {
            "keywords": ["soul-searching", "introspection", "solitude", "inner guidance"],
            "meaning": "Take time for solitude and reflection. The answers you seek are within. This is a period of inner work and spiritual development. Trust your own light."
        },
        "reversed": {
            "keywords": ["isolation", "loneliness", "withdrawal", "avoidance"],
            "meaning": "Too much isolation may be harmful. Balance solitude with connection. You may be avoiding necessary inner work or hiding from the world."
        }
    },
    {
        "name": "Wheel of Fortune",
        "number": 10,
        "emoji": "🎡",
        "upright": {
            "keywords": ["fortune", "karma", "cycles", "destiny", "change"],
            "meaning": "The wheel turns in your favor! Expect positive changes and lucky breaks. Karma is at work. Embrace the cycles of life and trust in divine timing."
        },
        "reversed": {
            "keywords": ["misfortune", "resistance", "stagnation"],
            "meaning": "You may be resisting necessary changes or experiencing a downturn. Remember that all cycles pass. Look for the lessons in this challenging time."
        }
    },
    {
        "name": "Justice",
        "number": 11,
        "emoji": "⚖️",
        "upright": {
            "keywords": ["justice", "fairness", "truth", "cause and effect", "law"],
            "meaning": "Truth and fairness prevail. Take responsibility for your actions and their consequences. Legal matters favor you. Make decisions based on logic and ethics."
        },
        "reversed": {
            "keywords": ["unfairness", "dishonesty", "unaccountability", "injustice"],
            "meaning": "Injustice or dishonesty may be present. Examine where you might be avoiding accountability. Seek truth even when it's uncomfortable."
        }
    },
    {
        "name": "The Hanged Man",
        "number": 12,
        "emoji": "🙃",
        "upright": {
            "keywords": ["pause", "surrender", "letting go", "new perspective"],
            "meaning": "Pause and see things from a different angle. Surrender control and trust the process. This period of suspension brings valuable insights and spiritual growth."
        },
        "reversed": {
            "keywords": ["delays", "resistance", "stalling", "indecision"],
            "meaning": "You may be resisting necessary surrender or stuck in indecision. Stop stalling and make a choice, even if it requires sacrifice."
        }
    },
    {
        "name": "Death",
        "number": 13,
        "emoji": "🦋",
        "upright": {
            "keywords": ["endings", "change", "transformation", "transition", "rebirth"],
            "meaning": "A powerful transformation is occurring. Let go of what no longer serves you. This ending makes way for beautiful new beginnings. Embrace the metamorphosis."
        },
        "reversed": {
            "keywords": ["resistance", "stagnation", "clinging"],
            "meaning": "You may be resisting an inevitable ending or change. Clinging to the past blocks your growth. Trust that transformation is necessary for evolution."
        }
    },
    {
        "name": "Temperance",
        "number": 14,
        "emoji": "⚗️",
        "upright": {
            "keywords": ["balance", "moderation", "patience", "purpose", "meaning"],
            "meaning": "Find middle ground and practice moderation. Patience brings rewards. Blend different aspects of your life harmoniously. Your guardian angels are near."
        },
        "reversed": {
            "keywords": ["imbalance", "excess", "self-healing", "re-alignment"],
            "meaning": "Life may feel out of balance. Excess in some area needs addressing. Take time to realign with your center and practice self-healing."
        }
    },
    {
        "name": "The Devil",
        "number": 15,
        "emoji": "⛓️",
        "upright": {
            "keywords": ["shadow self", "attachment", "addiction", "restriction", "sexuality"],
            "meaning": "Examine what binds you - addictions, unhealthy attachments, or limiting beliefs. You have more freedom than you realize. Face your shadow with honesty."
        },
        "reversed": {
            "keywords": ["release", "liberation", "detachment"],
            "meaning": "You're breaking free from restrictions and unhealthy patterns. Continue releasing what binds you. Liberation and self-awareness increase."
        }
    },
    {
        "name": "The Tower",
        "number": 16,
        "emoji": "⚡",
        "upright": {
            "keywords": ["sudden change", "upheaval", "chaos", "revelation", "awakening"],
            "meaning": "Sudden change shakes foundations, but this destruction clears the path for something better. Truth is revealed. Embrace this awakening, however uncomfortable."
        },
        "reversed": {
            "keywords": ["transformation", "resistance", "avoidance"],
            "meaning": "You may be resisting necessary upheaval or barely avoiding disaster. The change you fear may be exactly what you need. Let the old structures fall."
        }
    },
    {
        "name": "The Star",
        "number": 17,
        "emoji": "⭐",
        "upright": {
            "keywords": ["hope", "faith", "purpose", "renewal", "spirituality"],
            "meaning": "Hope shines bright after difficulty. You're entering a period of healing, inspiration, and renewed faith. Trust in the universe's plan. Your wishes manifest."
        },
        "reversed": {
            "keywords": ["lack of faith", "despair", "self-trust", "disconnection"],
            "meaning": "Hope feels distant, but it's still there. Reconnect with your faith and inner light. This darkness is temporary. Seek small moments of beauty."
        }
    },
    {
        "name": "The Moon",
        "number": 18,
        "emoji": "🌕",
        "upright": {
            "keywords": ["illusion", "fear", "anxiety", "subconscious", "intuition"],
            "meaning": "Things are not as they appear. Trust your intuition through this confusing time. Your subconscious sends important messages through dreams. Face your fears."
        },
        "reversed": {
            "keywords": ["release of fear", "unhappiness", "confusion", "misinterpretation"],
            "meaning": "Confusion clears and fears release. Hidden truths emerge. You're moving through illusion into clarity. Trust the process of revelation."
        }
    },
    {
        "name": "The Sun",
        "number": 19,
        "emoji": "☀️",
        "upright": {
            "keywords": ["positivity", "fun", "warmth", "success", "vitality"],
            "meaning": "Joy, success, and vitality shine upon you! This is a wonderful time of happiness, achievement, and celebration. Everything is illuminated. Embrace life fully."
        },
        "reversed": {
            "keywords": ["shadow", "sadness", "delusion", "ego"],
            "meaning": "Your inner light may be dimmed temporarily. Reconnect with simple joys and your inner child. Don't let ego block authentic happiness."
        }
    },
    {
        "name": "Judgement",
        "number": 20,
        "emoji": "📯",
        "upright": {
            "keywords": ["judgement", "rebirth", "inner calling", "absolution"],
            "meaning": "A spiritual awakening and life-changing decision await. Answer your higher calling. This is a time of reckoning, forgiveness, and rising to your true purpose."
        },
        "reversed": {
            "keywords": ["self-doubt", "judgment", "avoidance"],
            "meaning": "You may be ignoring an important calling or being too self-critical. Release judgment of self and others. Listen to what your soul truly wants."
        }
    },
    {
        "name": "The World",
        "number": 21,
        "emoji": "🌍",
        "upright": {
            "keywords": ["completion", "integration", "accomplishment", "travel"],
            "meaning": "A major cycle completes! You've achieved wholeness and integration. Celebrate your accomplishments. The world opens to you with new opportunities and adventures."
        },
        "reversed": {
            "keywords": ["incompletion", "shortcuts", "delays"],
            "meaning": "Completion feels just out of reach. Don't take shortcuts - finish what you started properly. Closure will come with patience and persistence."
        }
    }
]

MINOR_ARCANA_WANDS = [
    {
        "name": "Ace of Wands",
        "suit": "Wands",
        "number": 1,
        "emoji": "🪄",
        "upright": {
            "keywords": ["inspiration", "new opportunities", "growth", "potential"],
            "meaning": "A spark of inspiration ignites! New creative opportunities emerge. This is the seed of a passionate new venture. Act on your enthusiasm now."
        },
        "reversed": {
            "keywords": ["delays", "lack of motivation", "creative blocks"],
            "meaning": "Creative energy feels blocked or delayed. Reconnect with what inspires you. The spark is still there, waiting to be rekindled."
        }
    },
    {
        "name": "Two of Wands",
        "number": 2,
        "suit": "Wands",
        "emoji": "🗺️",
        "upright": {
            "keywords": ["vision", "progress", "decisions", "discovery"],
            "meaning": "You're planning your next move with the world at your feet. Make decisions about your future direction. Your vision expands beyond current horizons."
        },
        "reversed": {
            "keywords": ["fear", "hesitation", "limitation"],
            "meaning": "Fear of the unknown holds you back from expansion. You may be playing it too safe. Take calculated risks toward your dreams."
        }
    },
    {
        "name": "Three of Wands",
        "number": 3,
        "suit": "Wands",
        "emoji": "🚢",
        "upright": {
            "keywords": ["expansion", "foresight", "overseas opportunities"],
            "meaning": "Your efforts begin to bear fruit. Look toward expansion and long-term success. Opportunities from afar arrive. Your ships are coming in."
        },
        "reversed": {
            "keywords": ["limitation", "shortsightedness", "delays"],
            "meaning": "You may be limiting your vision or experiencing frustrating delays. Think bigger. Don't let setbacks stop your expansion plans."
        }
    },
    {
        "name": "Four of Wands",
        "number": 4,
        "suit": "Wands",
        "emoji": "🎊",
        "upright": {
            "keywords": ["celebration", "joy", "harmony", "homecoming"],
            "meaning": "Time to celebrate! A milestone is reached. Harmony in home and relationships. Community gathers in joy. Enjoy this moment of stability and happiness."
        },
        "reversed": {
            "keywords": ["instability", "discord", "conflict"],
            "meaning": "External celebration may be delayed, but inner contentment is available. There may be discord at home or within a community. Seek harmony."
        }
    },
    {
        "name": "Five of Wands",
        "number": 5,
        "suit": "Wands",
        "emoji": "🤺",
        "upright": {
            "keywords": ["conflict", "competition", "disagreement", "diversity"],
            "meaning": "Expect competition and conflicting viewpoints. This challenge builds strength. Channel competitive energy constructively. Stand your ground respectfully."
        },
        "reversed": {
            "keywords": ["avoidance", "resolution", "agreement"],
            "meaning": "Conflict resolves or is being avoided. Find common ground. Internal battles may need addressing. Choose your battles wisely."
        }
    },
    {
        "name": "Six of Wands",
        "number": 6,
        "suit": "Wands",
        "emoji": "🏅",
        "upright": {
            "keywords": ["success", "recognition", "progress", "confidence"],
            "meaning": "Victory and public recognition! Your efforts are acknowledged and celebrated. Confidence soars. Lead by example and accept praise graciously."
        },
        "reversed": {
            "keywords": ["setback", "ego", "doubt"],
            "meaning": "Success may be private rather than public. Watch for ego or others' jealousy. True confidence comes from within, not external validation."
        }
    },
    {
        "name": "Seven of Wands",
        "number": 7,
        "suit": "Wands",
        "emoji": "🛡️",
        "upright": {
            "keywords": ["challenge", "perseverance", "defense"],
            "meaning": "Stand your ground against opposition. Your position is challenged but defensible. Persevere with courage. Don't back down from what you believe in."
        },
        "reversed": {
            "keywords": ["exhaustion", "surrender", "overwhelm"],
            "meaning": "You may be exhausted from constant battles or ready to give up. Choose what's worth defending. Sometimes strategic retreat is wise."
        }
    },
    {
        "name": "Eight of Wands",
        "number": 8,
        "suit": "Wands",
        "emoji": "✈️",
        "upright": {
            "keywords": ["movement", "speed", "action", "travel"],
            "meaning": "Things accelerate rapidly! Swift movement and quick developments. Messages arrive, travel beckons. Strike while the iron is hot. Momentum builds."
        },
        "reversed": {
            "keywords": ["delays", "frustration", "waiting", "stagnation"],
            "meaning": "Frustrating delays slow your momentum. Practice patience. Use this time to prepare for when things speed up again."
        }
    },
    {
        "name": "Nine of Wands",
        "number": 9,
        "suit": "Wands",
        "emoji": "💪",
        "upright": {
            "keywords": ["resilience", "courage", "persistence", "boundaries"],
            "meaning": "You're battle-worn but not defeated. One last push is needed. Draw on your reserves of strength. Maintain healthy boundaries. Victory is close."
        },
        "reversed": {
            "keywords": ["exhaustion", "depletion", "overwhelm", "paranoia"],
            "meaning": "Exhaustion threatens to overwhelm. You may be too defensive or paranoid. Rest and recover. Know when to ask for help."
        }
    },
    {
        "name": "Ten of Wands",
        "number": 10,
        "suit": "Wands",
        "emoji": "😓",
        "upright": {
            "keywords": ["burden", "responsibility", "effort", "stress"],
            "meaning": "Heavy burdens weigh you down. Too many responsibilities demand attention. Success brings new pressures. Delegate or release what you can."
        },
        "reversed": {
            "keywords": ["release", "delegation", "breakdown"],
            "meaning": "You're learning to release burdens or heading toward burnout. Delegate responsibilities. You don't have to carry everything alone."
        }
    },
    {
        "name": "Page of Wands",
        "number": 11,
        "suit": "Wands",
        "emoji": "🌱",
        "upright": {
            "keywords": ["inspiration", "ideas", "discovery", "free spirit"],
            "meaning": "Fresh creative energy and new ideas spark enthusiasm. Embrace your inner adventurer. Explore new interests fearlessly. Good news about creative ventures."
        },
        "reversed": {
            "keywords": ["aimlessness", "procrastination", "distraction"],
            "meaning": "Creative energy is scattered or you're procrastinating on inspired ideas. Focus your enthusiasm. Don't let self-doubt extinguish your spark."
        }
    },
    {
        "name": "Knight of Wands",
        "number": 12,
        "suit": "Wands",
        "emoji": "🐎",
        "upright": {
            "keywords": ["energy", "passion", "adventure", "impulsiveness"],
            "meaning": "Bold action and passionate pursuit! Chase your dreams with fiery enthusiasm. Adventure calls. Be confident but watch for recklessness."
        },
        "reversed": {
            "keywords": ["haste", "chaos", "delays", "frustration"],
            "meaning": "Impulsive energy needs channeling. You may be rushing without direction or feeling frustrated by delays. Focus your fire constructively."
        }
    },
    {
        "name": "Queen of Wands",
        "number": 13,
        "suit": "Wands",
        "emoji": "🔥",
        "upright": {
            "keywords": ["courage", "confidence", "determination", "magnetism"],
            "meaning": "Embody fierce confidence and warm charisma. Lead with passion and inspire others. Your creative powers are at their peak. Be bold and magnetic."
        },
        "reversed": {
            "keywords": ["self-respect", "self-confidence", "jealousy"],
            "meaning": "Confidence may be shaken or turned to arrogance. Watch for jealousy - yours or others'. Reconnect with your authentic inner fire."
        }
    },
    {
        "name": "King of Wands",
        "number": 14,
        "suit": "Wands",
        "emoji": "🌅",
        "upright": {
            "keywords": ["leadership", "vision", "entrepreneur", "honor"],
            "meaning": "Visionary leadership and entrepreneurial success. Take charge with passion and integrity. Your natural charisma attracts followers and opportunities."
        },
        "reversed": {
            "keywords": ["impulsiveness", "dominance", "tyranny"],
            "meaning": "Leadership may become tyrannical or impulsive. Check your ego. True authority comes from wisdom and respect, not domination."
        }
    }
]

MINOR_ARCANA_CUPS = [
    {
        "name": "Ace of Cups",
        "suit": "Cups",
        "number": 1,
        "emoji": "💝",
        "upright": {
            "keywords": ["love", "emotion", "awakening", "creativity"],
            "meaning": "Love overflows! New emotional beginnings, deep feelings, and creative inspiration pour forth. Open your heart to receive blessings."
        },
        "reversed": {
            "keywords": ["self-love", "blockage", "emptiness"],
            "meaning": "Emotions may be blocked or you're seeking love externally. Fill your own cup first. Self-love is the foundation."
        }
    },
    {
        "name": "Two of Cups",
        "suit": "Cups",
        "number": 2,
        "emoji": "💑",
        "upright": {
            "keywords": ["union", "partnership", "attraction"],
            "meaning": "Beautiful connection! Partnership, romance, and mutual respect flourish. Two souls unite in harmony. This bond is blessed."
        },
        "reversed": {
            "keywords": ["self-love", "separation", "disharmony"],
            "meaning": "Relationship imbalance or separation. Focus on self-love before partnering. Heal the relationship with yourself first."
        }
    },
    {
        "name": "Three of Cups",
        "suit": "Cups",
        "number": 3,
        "emoji": "🥂",
        "upright": {
            "keywords": ["celebration", "friendship", "creativity", "community"],
            "meaning": "Celebrate with friends! Joyful gatherings, creative collaborations, and community support. Share your happiness with those you love."
        },
        "reversed": {
            "keywords": ["independence", "solitude", "gossip", "excess"],
            "meaning": "Social connections may feel draining or toxic. Take time alone to recharge. Watch for gossip or overindulgence."
        }
    },
    {
        "name": "Four of Cups",
        "suit": "Cups",
        "number": 4,
        "emoji": "😔",
        "upright": {
            "keywords": ["meditation", "contemplation", "apathy", "re-evaluation"],
            "meaning": "You may be so focused on what's missing that you're blind to offerings before you. Look around with fresh eyes. New opportunities await your notice."
        },
        "reversed": {
            "keywords": ["awareness", "opportunity", "motivation"],
            "meaning": "You're waking up from apathy and seeing new possibilities. Seize opportunities you previously overlooked. Motivation returns."
        }
    },
    {
        "name": "Five of Cups",
        "suit": "Cups",
        "number": 5,
        "emoji": "😢",
        "upright": {
            "keywords": ["regret", "failure", "disappointment", "pessimism"],
            "meaning": "Grief over loss clouds your vision. It's okay to mourn, but don't miss what remains. Two cups still stand. Hope persists."
        },
        "reversed": {
            "keywords": ["recovery", "healing", "acceptance"],
            "meaning": "You're beginning to heal and move forward. Accept the past and embrace what remains. Forgiveness brings freedom."
        }
    },
    {
        "name": "Six of Cups",
        "suit": "Cups",
        "number": 6,
        "emoji": "🧸",
        "upright": {
            "keywords": ["nostalgia", "memory", "innocence", "joy"],
            "meaning": "Sweet memories and childhood joy surface. Reconnect with your inner child or people from your past. Innocent happiness is available now."
        },
        "reversed": {
            "keywords": ["nostalgia", "forgiveness", "release"],
            "meaning": "Don't get stuck in nostalgia. The past informs but shouldn't imprison. Forgive old wounds and move forward."
        }
    },
    {
        "name": "Seven of Cups",
        "suit": "Cups",
        "number": 7,
        "emoji": "💭",
        "upright": {
            "keywords": ["opportunities", "choices", "fantasy", "illusion"],
            "meaning": "Many options appear but not all are real. Discern illusion from genuine opportunity. Ground your dreams in practical reality."
        },
        "reversed": {
            "keywords": ["alignment", "clarity", "focus"],
            "meaning": "Clarity emerges from confusion. You're aligning with what truly matters. Make choices based on values, not fantasy."
        }
    },
    {
        "name": "Eight of Cups",
        "suit": "Cups",
        "number": 8,
        "emoji": "🚶",
        "upright": {
            "keywords": ["disappointment", "abandonment", "withdrawal", "escapism"],
            "meaning": "Sometimes walking away is the bravest choice. Leave behind what no longer fulfills you. Seek deeper meaning on a new path."
        },
        "reversed": {
            "keywords": ["fear", "stagnation", "acceptance"],
            "meaning": "Fear keeps you in an unfulfilling situation. Find the courage to leave or the acceptance to stay with peace."
        }
    },
    {
        "name": "Nine of Cups",
        "suit": "Cups",
        "number": 9,
        "emoji": "😊",
        "upright": {
            "keywords": ["contentment", "satisfaction", "gratitude", "fulfillment"],
            "meaning": "The wish card! Emotional fulfillment and contentment. Your heart's desire manifests. Enjoy this blessed time of satisfaction."
        },
        "reversed": {
            "keywords": ["emptiness", "materialism", "dissatisfaction"],
            "meaning": "Seeking happiness in external things leaves you empty. True contentment comes from within. Examine what really fulfills you."
        }
    },
    {
        "name": "Ten of Cups",
        "suit": "Cups",
        "number": 10,
        "emoji": "🌈",
        "upright": {
            "keywords": ["love", "harmony", "alignment", "family"],
            "meaning": "The happily ever after card! Complete emotional fulfillment. Family harmony and lasting happiness. Your heart overflows with love."
        },
        "reversed": {
            "keywords": ["disconnection", "misalignment", "discord"],
            "meaning": "Family or relationship discord. The perfect picture has cracks. Work toward authentic harmony rather than surface appearances."
        }
    },
    {
        "name": "Page of Cups",
        "suit": "Cups",
        "number": 11,
        "emoji": "🐟",
        "upright": {
            "keywords": ["creativity", "intuition", "curiosity"],
            "meaning": "Messages of love and creative inspiration arrive. Follow your intuition and inner child. Emotional and artistic growth beckon."
        },
        "reversed": {
            "keywords": ["immaturity", "blockage", "insecurity"],
            "meaning": "Emotional immaturity or creative blocks need attention. Don't let insecurity silence your intuition. Nurture your sensitive side."
        }
    },
    {
        "name": "Knight of Cups",
        "suit": "Cups",
        "number": 12,
        "emoji": "🦢",
        "upright": {
            "keywords": ["romance", "charm", "imagination", "devotion"],
            "meaning": "A romantic, creative soul follows their heart. Love proposals and artistic offers arrive. Lead with emotion and imagination."
        },
        "reversed": {
            "keywords": ["fantasy", "moodiness", "disappointment"],
            "meaning": "Romantic idealism may lead to disappointment. Ground your emotions in reality. Watch for moodiness or manipulation."
        }
    },
    {
        "name": "Queen of Cups",
        "suit": "Cups",
        "number": 13,
        "emoji": "🌊",
        "upright": {
            "keywords": ["compassion", "calm", "intuition", "security"],
            "meaning": "The embodiment of emotional wisdom and intuition. Nurture yourself and others with compassion. Trust your deep inner knowing."
        },
        "reversed": {
            "keywords": ["self-care", "emotional instability", "codependency"],
            "meaning": "Your giving nature may be depleted. Practice self-care before caring for others. Watch for codependency or emotional manipulation."
        }
    },
    {
        "name": "King of Cups",
        "suit": "Cups",
        "number": 14,
        "emoji": "🔱",
        "upright": {
            "keywords": ["balance", "compassion", "diplomacy"],
            "meaning": "Master of emotions who leads with heart and wisdom. Balance feeling with thinking. Your calm presence helps others through storms."
        },
        "reversed": {
            "keywords": ["repression", "depth", "moodiness"],
            "meaning": "Emotions may be suppressed or out of control. Find healthy emotional expression. Don't let sensitivity become manipulation."
        }
    }
]

MINOR_ARCANA_SWORDS = [
    {
        "name": "Ace of Swords",
        "suit": "Swords",
        "number": 1,
        "emoji": "⚔️",
        "upright": {
            "keywords": ["breakthrough", "clarity", "truth", "insight"],
            "meaning": "Mental breakthrough! Cut through confusion with crystal clarity. Truth pierces illusion. New ideas and intellectual victories emerge."
        },
        "reversed": {
            "keywords": ["confusion", "chaos", "fog"],
            "meaning": "Mental fog or confusion blocks clear thinking. Seek inner clarity before acting. The truth may be painful to face."
        }
    },
    {
        "name": "Two of Swords",
        "suit": "Swords",
        "number": 2,
        "emoji": "🤔",
        "upright": {
            "keywords": ["decisions", "deliberation", "stalemate"],
            "meaning": "A difficult decision requires careful consideration. You may be avoiding choosing. Remove the blindfold and face the choice honestly."
        },
        "reversed": {
            "keywords": ["indecision", "confusion", "overwhelm"],
            "meaning": "Paralysis by analysis or finally making a decision. Too much information confuses. Trust your gut and choose."
        }
    },
    {
        "name": "Three of Swords",
        "suit": "Swords",
        "number": 3,
        "emoji": "💔",
        "upright": {
            "keywords": ["heartbreak", "sorrow", "grief", "truth"],
            "meaning": "Heartbreak and emotional pain must be felt to heal. A painful truth emerges. Allow yourself to grieve fully."
        },
        "reversed": {
            "keywords": ["recovery", "forgiveness", "healing"],
            "meaning": "Healing from heartbreak begins. Forgiveness releases pain. The worst is over; recovery and hope return."
        }
    },
    {
        "name": "Four of Swords",
        "suit": "Swords",
        "number": 4,
        "emoji": "😴",
        "upright": {
            "keywords": ["rest", "restoration", "contemplation", "relaxation"],
            "meaning": "Rest is essential now. Retreat, restore, and recover. Mental burnout requires stillness. Peace comes through quiet contemplation."
        },
        "reversed": {
            "keywords": ["exhaustion", "burn-out", "stress"],
            "meaning": "You're not getting the rest you need or are finally recovering. Continued stress leads to breakdown. Prioritize restoration."
        }
    },
    {
        "name": "Five of Swords",
        "suit": "Swords",
        "number": 5,
        "emoji": "😤",
        "upright": {
            "keywords": ["conflict", "defeat", "loss"],
            "meaning": "A hollow victory or painful defeat. Conflict leaves everyone wounded. Consider if winning is worth the cost."
        },
        "reversed": {
            "keywords": ["reconciliation", "forgiveness", "release"],
            "meaning": "Time to end conflicts and move on. Seek reconciliation where possible. Learn from battles and release resentment."
        }
    },
    {
        "name": "Six of Swords",
        "suit": "Swords",
        "number": 6,
        "emoji": "⛵",
        "upright": {
            "keywords": ["transition", "departure", "passage"],
            "meaning": "Moving toward calmer waters. Leave troubles behind and transition to peace. The journey may be difficult but leads to better shores."
        },
        "reversed": {
            "keywords": ["baggage", "stagnation", "resistance"],
            "meaning": "You may be resisting necessary change or carrying too much baggage into new situations. Release and move forward."
        }
    },
    {
        "name": "Seven of Swords",
        "suit": "Swords",
        "number": 7,
        "emoji": "🥷",
        "upright": {
            "keywords": ["deception", "strategy", "stealth", "escape"],
            "meaning": "Someone may be acting deceptively - possibly you. Strategic thinking is needed. Not everything is as it appears."
        },
        "reversed": {
            "keywords": ["confession", "conscience", "honesty"],
            "meaning": "Secrets are revealed or conscience demands honesty. Come clean and face consequences. Deception backfires."
        }
    },
    {
        "name": "Eight of Swords",
        "suit": "Swords",
        "number": 8,
        "emoji": "🏚️",
        "upright": {
            "keywords": ["imprisonment", "limitation", "entrapment"],
            "meaning": "You feel trapped but the prison is largely of your own making. Limiting beliefs bind you. The path to freedom exists if you look."
        },
        "reversed": {
            "keywords": ["self-acceptance", "freedom", "release"],
            "meaning": "Breaking free from mental prisons. Self-imposed limitations lift. You see clearly now that escape was always possible."
        }
    },
    {
        "name": "Nine of Swords",
        "suit": "Swords",
        "number": 9,
        "emoji": "😰",
        "upright": {
            "keywords": ["anxiety", "worry", "fear", "nightmares"],
            "meaning": "Anxiety and dark thoughts disturb your peace. Worry may be out of proportion to reality. Seek support and perspective."
        },
        "reversed": {
            "keywords": ["turmoil", "secrets", "relief"],
            "meaning": "Anxiety begins to lift or inner turmoil needs addressing. Face your fears in daylight. Support is available."
        }
    },
    {
        "name": "Ten of Swords",
        "suit": "Swords",
        "number": 10,
        "emoji": "😵",
        "upright": {
            "keywords": ["endings", "betrayal", "loss", "crisis"],
            "meaning": "Rock bottom. A painful ending or betrayal. But this is the end of suffering - it can only get better from here. Dawn approaches."
        },
        "reversed": {
            "keywords": ["recovery", "regeneration", "resistance"],
            "meaning": "Recovery begins from a difficult time, or you're prolonging an inevitable ending. Release and allow healing to begin."
        }
    },
    {
        "name": "Page of Swords",
        "suit": "Swords",
        "number": 11,
        "emoji": "🔍",
        "upright": {
            "keywords": ["curiosity", "restlessness", "alertness"],
            "meaning": "Sharp mind eager to learn and communicate. New ideas and information arrive. Channel mental energy productively."
        },
        "reversed": {
            "keywords": ["haste", "gossip", "harm"],
            "meaning": "Mental energy turns destructive through gossip or hasty words. Think before speaking. Channel restlessness constructively."
        }
    },
    {
        "name": "Knight of Swords",
        "suit": "Swords",
        "number": 12,
        "emoji": "🌪️",
        "upright": {
            "keywords": ["ambition", "speed", "drive", "focus"],
            "meaning": "Charging forward with determination! Ambitious pursuit of goals. Quick thinking and action. Just don't run over others in your rush."
        },
        "reversed": {
            "keywords": ["restlessness", "chaos", "recklessness"],
            "meaning": "Ambition becomes recklessness or energy scatters without focus. Slow down before mistakes happen. Think before charging."
        }
    },
    {
        "name": "Queen of Swords",
        "suit": "Swords",
        "number": 13,
        "emoji": "👸",
        "upright": {
            "keywords": ["independence", "objectivity", "boundaries", "directness"],
            "meaning": "Clear-minded and discerning. Set boundaries with compassion. Your honest, direct communication cuts through confusion."
        },
        "reversed": {
            "keywords": ["coldness", "cruelty", "bitterness", "criticism"],
            "meaning": "Sharp intellect becomes cutting cruelty. Guard against bitterness and overly harsh judgment. Seek balance between head and heart."
        }
    },
    {
        "name": "King of Swords",
        "suit": "Swords",
        "number": 14,
        "emoji": "🗡️",
        "upright": {
            "keywords": ["intellect", "authority", "truth", "ethics"],
            "meaning": "Mastery of mind and truth. Lead with clear thinking and ethical authority. Your intellect serves justice and wisdom."
        },
        "reversed": {
            "keywords": ["manipulation", "tyranny", "abuse"],
            "meaning": "Intellectual power becomes manipulation or tyranny. Reason without compassion is cold. Balance authority with empathy."
        }
    }
]

MINOR_ARCANA_PENTACLES = [
    {
        "name": "Ace of Pentacles",
        "suit": "Pentacles",
        "number": 1,
        "emoji": "💰",
        "upright": {
            "keywords": ["opportunity", "manifestation", "abundance"],
            "meaning": "A golden opportunity for material success! New income, career opportunities, or investments bear fruit. Plant seeds of abundance."
        },
        "reversed": {
            "keywords": ["loss", "scarcity", "instability"],
            "meaning": "Financial opportunity may slip away or scarcity mindset blocks abundance. Ground yourself and look for practical solutions."
        }
    },
    {
        "name": "Two of Pentacles",
        "suit": "Pentacles",
        "number": 2,
        "emoji": "🤹",
        "upright": {
            "keywords": ["balance", "adaptability", "time management", "priorities"],
            "meaning": "Juggling multiple responsibilities with skill. Stay flexible and adaptable. Balance work, finances, and life with grace."
        },
        "reversed": {
            "keywords": ["overwhelm", "disorganization", "chaos"],
            "meaning": "Too many balls in the air threaten to drop. Overwhelm signals need to simplify. Prioritize and delegate."
        }
    },
    {
        "name": "Three of Pentacles",
        "suit": "Pentacles",
        "number": 3,
        "emoji": "🏗️",
        "upright": {
            "keywords": ["teamwork", "collaboration", "learning", "implementation"],
            "meaning": "Teamwork creates masterpieces. Collaborate with skilled others. Your work is recognized and valued. Build something lasting together."
        },
        "reversed": {
            "keywords": ["disharmony", "misalignment", "solitude"],
            "meaning": "Team conflict or misaligned goals hinder progress. Communication problems need addressing. Perhaps working alone suits better now."
        }
    },
    {
        "name": "Four of Pentacles",
        "suit": "Pentacles",
        "number": 4,
        "emoji": "🏦",
        "upright": {
            "keywords": ["saving", "security", "conservatism", "scarcity"],
            "meaning": "Holding onto resources tightly. Financial security through saving. But don't let fear of loss become hoarding that blocks flow."
        },
        "reversed": {
            "keywords": ["generosity", "spending", "insecurity"],
            "meaning": "Learning to release grip on money or material things. Generosity flows or reckless spending occurs. Find healthy balance."
        }
    },
    {
        "name": "Five of Pentacles",
        "suit": "Pentacles",
        "number": 5,
        "emoji": "🥶",
        "upright": {
            "keywords": ["financial loss", "poverty", "lack", "isolation"],
            "meaning": "Hard times and feelings of lack or exclusion. Help is available if you look. Don't let pride keep you from support."
        },
        "reversed": {
            "keywords": ["recovery", "spiritual wealth", "improvement"],
            "meaning": "Financial recovery begins. Worst times pass. Spiritual wealth matters more than material. Accept help offered."
        }
    },
    {
        "name": "Six of Pentacles",
        "suit": "Pentacles",
        "number": 6,
        "emoji": "🎁",
        "upright": {
            "keywords": ["giving", "receiving", "sharing", "generosity"],
            "meaning": "Generosity flows both ways. Give and receive with open heart. Balance between helping others and accepting help yourself."
        },
        "reversed": {
            "keywords": ["conditions", "imbalance", "power"],
            "meaning": "Giving may have strings attached or receiving feels uncomfortable. Examine power dynamics in exchanges. Seek true generosity."
        }
    },
    {
        "name": "Seven of Pentacles",
        "suit": "Pentacles",
        "number": 7,
        "emoji": "🌾",
        "upright": {
            "keywords": ["patience", "perseverance", "investment", "reward"],
            "meaning": "Patience with slow-growing investments. Your efforts will pay off in time. Assess progress but don't abandon the garden."
        },
        "reversed": {
            "keywords": ["stagnation", "impatience", "loss"],
            "meaning": "Impatience with slow results or concern about wasted effort. Reassess strategy. Some investments may not be worth continuing."
        }
    },
    {
        "name": "Eight of Pentacles",
        "suit": "Pentacles",
        "number": 8,
        "emoji": "🔨",
        "upright": {
            "keywords": ["apprenticeship", "skill development", "diligence", "mastery"],
            "meaning": "Dedicated effort builds mastery. Focus on skill development and quality work. Your diligence attracts recognition and rewards."
        },
        "reversed": {
            "keywords": ["perfectionism", "distraction", "tedium"],
            "meaning": "Work feels uninspiring or perfectionism paralyzes. Reconnect with purpose behind the effort. Quality matters but so does completion."
        }
    },
    {
        "name": "Nine of Pentacles",
        "suit": "Pentacles",
        "number": 9,
        "emoji": "🍇",
        "upright": {
            "keywords": ["abundance", "luxury", "self-sufficiency", "independence"],
            "meaning": "Enjoying fruits of your labor in comfort and abundance. Financial independence achieved. Savor life's luxuries - you've earned them."
        },
        "reversed": {
            "keywords": ["self-worth", "setback", "imbalance"],
            "meaning": "Material success may mask inner emptiness, or financial setbacks threaten comfort. True abundance includes more than money."
        }
    },
    {
        "name": "Ten of Pentacles",
        "suit": "Pentacles",
        "number": 10,
        "emoji": "🏰",
        "upright": {
            "keywords": ["wealth", "inheritance", "family", "establishment"],
            "meaning": "Legacy wealth and family abundance. Long-term financial security. The fruits of generations of effort. Prosperity to share."
        },
        "reversed": {
            "keywords": ["loss", "conflict", "instability"],
            "meaning": "Family financial disputes or legacy issues. Material foundations may be unstable. Don't sacrifice relationships for money."
        }
    },
    {
        "name": "Page of Pentacles",
        "suit": "Pentacles",
        "number": 11,
        "emoji": "📚",
        "upright": {
            "keywords": ["manifestation", "opportunity", "learning"],
            "meaning": "New opportunity for learning and earning. Practical skills develop. Stay grounded while pursuing ambitious material goals."
        },
        "reversed": {
            "keywords": ["stagnation", "procrastination", "lessons"],
            "meaning": "Material goals stall or practical learning is avoided. Don't let fear of failure stop you from starting. Learn by doing."
        }
    },
    {
        "name": "Knight of Pentacles",
        "suit": "Pentacles",
        "number": 12,
        "emoji": "🐢",
        "upright": {
            "keywords": ["diligence", "routine", "responsibility", "persistence"],
            "meaning": "Slow and steady wins the race. Hard work and routine build lasting results. Dependable effort leads to success."
        },
        "reversed": {
            "keywords": ["stagnation", "boredom", "laziness", "inertia"],
            "meaning": "Routine becomes rut or discipline slips into laziness. Find motivation. Break patterns that no longer serve progress."
        }
    },
    {
        "name": "Queen of Pentacles",
        "suit": "Pentacles",
        "number": 13,
        "emoji": "🌻",
        "upright": {
            "keywords": ["nurturing", "practicality", "provision", "abundance"],
            "meaning": "Abundant nurturer who creates comfort and security. Practical wisdom guides material success. Care for self and others generously."
        },
        "reversed": {
            "keywords": ["self-care", "conflict", "insecurity"],
            "meaning": "Neglecting self while nurturing others, or material concerns overwhelming care. Balance giving with receiving self-care."
        }
    },
    {
        "name": "King of Pentacles",
        "suit": "Pentacles",
        "number": 14,
        "emoji": "💎",
        "upright": {
            "keywords": ["wealth", "business", "leadership", "security"],
            "meaning": "Master of material realm. Business success through wise management. Security and abundance achieved through discipline and vision."
        },
        "reversed": {
            "keywords": ["greed", "materialism", "instability"],
            "meaning": "Material success corrupts or proves unstable. Greed or obsession with wealth damages other life areas. Reassess values."
        }
    }
]

# Combine all cards
ALL_CARDS = MAJOR_ARCANA + MINOR_ARCANA_WANDS + MINOR_ARCANA_CUPS + MINOR_ARCANA_SWORDS + MINOR_ARCANA_PENTACLES

def get_all_cards():
    """Return all 78 tarot cards"""
    return ALL_CARDS

def get_major_arcana():
    """Return only Major Arcana cards"""
    return MAJOR_ARCANA

def get_minor_arcana():
    """Return all Minor Arcana cards"""
    return MINOR_ARCANA_WANDS + MINOR_ARCANA_CUPS + MINOR_ARCANA_SWORDS + MINOR_ARCANA_PENTACLES
