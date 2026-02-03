"""
Tense-based reflection prompts for each tarot card
Each card has past/present/future versions for both upright and reversed
"""

CARD_REFLECTIONS = {
    # === MAJOR ARCANA ===
    "The Fool": {
        "upright": {
            "past": "What leap was taken?",
            "present": "What is beginning?",
            "future": "What calls to be explored?"
        },
        "reversed": {
            "past": "What hesitation held things back?",
            "present": "What holds back the leap?",
            "future": "What caution may be needed?"
        }
    },
    "The Magician": {
        "upright": {
            "past": "What was brought into being?",
            "present": "What power is ready to be used?",
            "future": "What may be manifested?"
        },
        "reversed": {
            "past": "What potential went untapped?",
            "present": "What power lies dormant?",
            "future": "What illusion may distract?"
        }
    },
    "The High Priestess": {
        "upright": {
            "past": "What did the inner knowing reveal?",
            "present": "What whispers from within?",
            "future": "What hidden truth will surface?"
        },
        "reversed": {
            "past": "What inner voice was ignored?",
            "present": "What remains veiled?",
            "future": "What may stay hidden?"
        }
    },
    "The Empress": {
        "upright": {
            "past": "What abundance was cultivated?",
            "present": "Where is growth flourishing?",
            "future": "What nurturing will bear fruit?"
        },
        "reversed": {
            "past": "What was neglected or blocked?",
            "present": "What needs nurturing attention?",
            "future": "What may wither without care?"
        }
    },
    "The Emperor": {
        "upright": {
            "past": "What structure was built?",
            "present": "Where is order needed?",
            "future": "What will be established?"
        },
        "reversed": {
            "past": "Where did rigidity take hold?",
            "present": "What grip needs loosening?",
            "future": "What rigidity may cause harm?"
        }
    },
    "The Hierophant": {
        "upright": {
            "past": "What wisdom was passed down?",
            "present": "What is being learned or taught?",
            "future": "What guidance will come?"
        },
        "reversed": {
            "past": "What was questioned?",
            "present": "What no longer rings true?",
            "future": "What inner truth will emerge?"
        }
    },
    "The Lovers": {
        "upright": {
            "past": "What choice was made from the heart?",
            "present": "What is coming together?",
            "future": "What union awaits?"
        },
        "reversed": {
            "past": "Where did things fall out of alignment?",
            "present": "What feels divided?",
            "future": "What may pull apart?"
        }
    },
    "The Chariot": {
        "upright": {
            "past": "What was overcome through will?",
            "present": "What drives forward?",
            "future": "What victory awaits?"
        },
        "reversed": {
            "past": "Where was momentum lost?",
            "present": "What pulls in different directions?",
            "future": "What may stall?"
        }
    },
    "Strength": {
        "upright": {
            "past": "What was gently overcome?",
            "present": "Where does quiet power reside?",
            "future": "What will be tamed with patience?"
        },
        "reversed": {
            "past": "What inner struggle weakened resolve?",
            "present": "What inner fire needs rekindling?",
            "future": "What doubt may rise?"
        }
    },
    "The Hermit": {
        "upright": {
            "past": "What wisdom came from solitude?",
            "present": "What truth is found in stillness?",
            "future": "What will inner reflection reveal?"
        },
        "reversed": {
            "past": "What solitude became too heavy?",
            "present": "What withdrawal now burdens?",
            "future": "What connection may be needed?"
        }
    },
    "Wheel of Fortune": {
        "upright": {
            "past": "What turned?",
            "present": "What is shifting?",
            "future": "What change approaches?"
        },
        "reversed": {
            "past": "What turn was resisted?",
            "present": "What feels stuck in a cycle?",
            "future": "What downturn may pass?"
        }
    },
    "Justice": {
        "upright": {
            "past": "What came into balance?",
            "present": "What is being weighed?",
            "future": "What will be set right?"
        },
        "reversed": {
            "past": "What fell out of balance?",
            "present": "What feels unjust?",
            "future": "What may escape reckoning?"
        }
    },
    "The Hanged Man": {
        "upright": {
            "past": "What was seen from a new angle?",
            "present": "What asks for surrender?",
            "future": "What will come through letting go?"
        },
        "reversed": {
            "past": "What was avoided?",
            "present": "What stalling persists?",
            "future": "What resistance may cost?"
        }
    },
    "Death": {
        "upright": {
            "past": "What ended to make way?",
            "present": "What is transforming?",
            "future": "What must fall away?"
        },
        "reversed": {
            "past": "What ending was resisted?",
            "present": "What clings to what was?",
            "future": "What change may be prolonged?"
        }
    },
    "Temperance": {
        "upright": {
            "past": "What found its balance?",
            "present": "What is being blended?",
            "future": "What harmony will emerge?"
        },
        "reversed": {
            "past": "What tipped too far?",
            "present": "What has grown excessive?",
            "future": "What imbalance may grow?"
        }
    },
    "The Devil": {
        "upright": {
            "past": "What held things captive?",
            "present": "What binds?",
            "future": "What shadow must be faced?"
        },
        "reversed": {
            "past": "What chains were loosened?",
            "present": "What is breaking free?",
            "future": "What release awaits?"
        }
    },
    "The Tower": {
        "upright": {
            "past": "What came crashing down?",
            "present": "What is being shaken?",
            "future": "What will shatter?"
        },
        "reversed": {
            "past": "What collapse was averted?",
            "present": "What trembles but holds?",
            "future": "What may yet fall?"
        }
    },
    "The Star": {
        "upright": {
            "past": "What light guided through darkness?",
            "present": "Where does hope shine?",
            "future": "What healing awaits?"
        },
        "reversed": {
            "past": "What dimmed the light?",
            "present": "What hope flickers?",
            "future": "What faith may waver?"
        }
    },
    "The Moon": {
        "upright": {
            "past": "What moved in shadow?",
            "present": "What is unclear?",
            "future": "What will emerge from darkness?"
        },
        "reversed": {
            "past": "What became clear?",
            "present": "What fog is lifting?",
            "future": "What will come to light?"
        }
    },
    "The Sun": {
        "upright": {
            "past": "What brought light?",
            "present": "What shines bright?",
            "future": "What joy awaits?"
        },
        "reversed": {
            "past": "What cast a shadow?",
            "present": "What dims the light?",
            "future": "What brightness may fade?"
        }
    },
    "Judgement": {
        "upright": {
            "past": "What was awakened?",
            "present": "What is rising?",
            "future": "What reckoning awaits?"
        },
        "reversed": {
            "past": "What call went unheard?",
            "present": "What weighs without release?",
            "future": "What rising may be delayed?"
        }
    },
    "The World": {
        "upright": {
            "past": "What came full circle?",
            "present": "What is completing?",
            "future": "What wholeness awaits?"
        },
        "reversed": {
            "past": "What was left unfinished?",
            "present": "What lacks completion?",
            "future": "What closure may wait?"
        }
    },

    # === WANDS ===
    "Ace of Wands": {
        "upright": {
            "past": "What spark ignited?",
            "present": "What is catching fire?",
            "future": "What spark awaits?"
        },
        "reversed": {
            "past": "What spark faded?",
            "present": "What dampens the flame?",
            "future": "What fire may be lacking?"
        }
    },
    "Two of Wands": {
        "upright": {
            "past": "What vision was set in motion?",
            "present": "What is being envisioned?",
            "future": "What horizon awaits?"
        },
        "reversed": {
            "past": "What kept the gaze too narrow?",
            "present": "What holds back the reach?",
            "future": "What vision may be limited?"
        }
    },
    "Three of Wands": {
        "upright": {
            "past": "What began to bear fruit?",
            "present": "What is coming into view?",
            "future": "What waits on the horizon?"
        },
        "reversed": {
            "past": "What growth was blocked?",
            "present": "What delays linger?",
            "future": "What may be slow to arrive?"
        }
    },
    "Four of Wands": {
        "upright": {
            "past": "What was celebrated?",
            "present": "What stability holds?",
            "future": "What joy approaches?"
        },
        "reversed": {
            "past": "What disrupted the peace?",
            "present": "What unsettles?",
            "future": "What instability may arise?"
        }
    },
    "Five of Wands": {
        "upright": {
            "past": "What struggle tested strength?",
            "present": "What friction stirs?",
            "future": "What challenge approaches?"
        },
        "reversed": {
            "past": "What conflict eased?",
            "present": "What fight is ending?",
            "future": "What tension may ease?"
        }
    },
    "Six of Wands": {
        "upright": {
            "past": "What triumph was won?",
            "present": "What rises victorious?",
            "future": "What success awaits?"
        },
        "reversed": {
            "past": "What went unacknowledged?",
            "present": "What falters in confidence?",
            "future": "What may stumble?"
        }
    },
    "Seven of Wands": {
        "upright": {
            "past": "What ground was held?",
            "present": "What requires standing firm?",
            "future": "What must be defended?"
        },
        "reversed": {
            "past": "What fight wore down?",
            "present": "What resistance exhausts?",
            "future": "What may be time to yield?"
        }
    },
    "Eight of Wands": {
        "upright": {
            "past": "What flew forward?",
            "present": "What is in motion?",
            "future": "What will arrive swiftly?"
        },
        "reversed": {
            "past": "What was delayed?",
            "present": "What slows?",
            "future": "What may be held back?"
        }
    },
    "Nine of Wands": {
        "upright": {
            "past": "What was endured?",
            "present": "What strength remains?",
            "future": "What will require perseverance?"
        },
        "reversed": {
            "past": "What wore down?",
            "present": "What weariness weighs?",
            "future": "What may deplete?"
        }
    },
    "Ten of Wands": {
        "upright": {
            "past": "What weight was carried?",
            "present": "What weighs heavy?",
            "future": "What burden may grow?"
        },
        "reversed": {
            "past": "What was set down?",
            "present": "What seeks release?",
            "future": "What relief awaits?"
        }
    },
    "Page of Wands": {
        "upright": {
            "past": "What curiosity sparked?",
            "present": "What beckons to be explored?",
            "future": "What new energy awaits?"
        },
        "reversed": {
            "past": "What never took flight?",
            "present": "What lacks direction?",
            "future": "What spark may fizzle?"
        }
    },
    "Knight of Wands": {
        "upright": {
            "past": "What was chased with fire?",
            "present": "What charges forward?",
            "future": "What calls for bold action?"
        },
        "reversed": {
            "past": "What rushed too fast?",
            "present": "What burns without direction?",
            "future": "What haste may cost?"
        }
    },
    "Queen of Wands": {
        "upright": {
            "past": "What radiance led the way?",
            "present": "What burns with warmth?",
            "future": "What will shine boldly?"
        },
        "reversed": {
            "past": "What dimmed the inner fire?",
            "present": "What warmth needs rekindling?",
            "future": "What flame may flicker?"
        }
    },
    "King of Wands": {
        "upright": {
            "past": "What vision blazed into being?",
            "present": "What commands with fire?",
            "future": "What will be forged?"
        },
        "reversed": {
            "past": "What burned too hot?",
            "present": "What force needs softening?",
            "future": "What may burn out of control?"
        }
    },

    # === CUPS ===
    "Ace of Cups": {
        "upright": {
            "past": "What opened?",
            "present": "What overflows?",
            "future": "What will fill the heart?"
        },
        "reversed": {
            "past": "What was blocked?",
            "present": "What runs dry?",
            "future": "What emptiness may come?"
        }
    },
    "Two of Cups": {
        "upright": {
            "past": "What came together?",
            "present": "What flows between?",
            "future": "What connection will deepen?"
        },
        "reversed": {
            "past": "What drifted apart?",
            "present": "What disconnection aches?",
            "future": "What bond may strain?"
        }
    },
    "Three of Cups": {
        "upright": {
            "past": "What was celebrated together?",
            "present": "What joy is shared?",
            "future": "What gathering awaits?"
        },
        "reversed": {
            "past": "What celebration soured?",
            "present": "What feels isolated?",
            "future": "What togetherness may falter?"
        }
    },
    "Four of Cups": {
        "upright": {
            "past": "What went unnoticed?",
            "present": "What is being overlooked?",
            "future": "What may be missed?"
        },
        "reversed": {
            "past": "What stirred awake?",
            "present": "What is being seen anew?",
            "future": "What awareness will emerge?"
        }
    },
    "Five of Cups": {
        "upright": {
            "past": "What was mourned?",
            "present": "What grief lingers?",
            "future": "What loss may come?"
        },
        "reversed": {
            "past": "What began to heal?",
            "present": "What is being released?",
            "future": "What healing awaits?"
        }
    },
    "Six of Cups": {
        "upright": {
            "past": "What sweet memory returned?",
            "present": "What echoes from before?",
            "future": "What from the past will return?"
        },
        "reversed": {
            "past": "What kept things looking back?",
            "present": "What clings to what was?",
            "future": "What past must be released?"
        }
    },
    "Seven of Cups": {
        "upright": {
            "past": "What dream drifted?",
            "present": "What clouds the vision?",
            "future": "What illusion may tempt?"
        },
        "reversed": {
            "past": "What came into focus?",
            "present": "What is becoming clear?",
            "future": "What clarity awaits?"
        }
    },
    "Eight of Cups": {
        "upright": {
            "past": "What was walked away from?",
            "present": "What calls to be left?",
            "future": "What will be departed?"
        },
        "reversed": {
            "past": "What couldn't be left?",
            "present": "What keeps holding on?",
            "future": "What may be hard to leave?"
        }
    },
    "Nine of Cups": {
        "upright": {
            "past": "What was wished and granted?",
            "present": "What satisfies deeply?",
            "future": "What fulfillment awaits?"
        },
        "reversed": {
            "past": "What felt hollow?",
            "present": "What satisfaction lacks depth?",
            "future": "What may disappoint?"
        }
    },
    "Ten of Cups": {
        "upright": {
            "past": "What brought deep fulfillment?",
            "present": "What harmony blesses?",
            "future": "What wholeness awaits?"
        },
        "reversed": {
            "past": "What harmony fractured?",
            "present": "What aches to be whole?",
            "future": "What peace may be tested?"
        }
    },
    "Page of Cups": {
        "upright": {
            "past": "What stirred the heart?",
            "present": "What gentle message comes?",
            "future": "What new feeling will emerge?"
        },
        "reversed": {
            "past": "What tenderness was bruised?",
            "present": "What softness hardens?",
            "future": "What may close off?"
        }
    },
    "Knight of Cups": {
        "upright": {
            "past": "What was followed with heart?",
            "present": "What moves with feeling?",
            "future": "What will arrive bearing emotion?"
        },
        "reversed": {
            "past": "What dream disappointed?",
            "present": "What churns beneath?",
            "future": "What feeling may deceive?"
        }
    },
    "Queen of Cups": {
        "upright": {
            "past": "What depth was held with care?",
            "present": "What flows with knowing?",
            "future": "What will be held gently?"
        },
        "reversed": {
            "past": "What depths overwhelmed?",
            "present": "What pours out too freely?",
            "future": "What may flood or drown?"
        }
    },
    "King of Cups": {
        "upright": {
            "past": "What was navigated with calm?",
            "present": "What rests in still waters?",
            "future": "What will be mastered through depth?"
        },
        "reversed": {
            "past": "What was pushed under?",
            "present": "What stirs in the deep?",
            "future": "What may surface uncontrolled?"
        }
    },

    # === SWORDS ===
    "Ace of Swords": {
        "upright": {
            "past": "What cut through?",
            "present": "What becomes clear?",
            "future": "What truth will emerge?"
        },
        "reversed": {
            "past": "What remained unclear?",
            "present": "What clouds the mind?",
            "future": "What confusion may come?"
        }
    },
    "Two of Swords": {
        "upright": {
            "past": "What choice was weighed?",
            "present": "What hangs in balance?",
            "future": "What decision approaches?"
        },
        "reversed": {
            "past": "What deadlock broke?",
            "present": "What can no longer be avoided?",
            "future": "What must be faced?"
        }
    },
    "Three of Swords": {
        "upright": {
            "past": "What pierced the heart?",
            "present": "What aches?",
            "future": "What may wound?"
        },
        "reversed": {
            "past": "What began to mend?",
            "present": "What heals?",
            "future": "What will heal?"
        }
    },
    "Four of Swords": {
        "upright": {
            "past": "What rest was taken?",
            "present": "What needs stillness?",
            "future": "What pause awaits?"
        },
        "reversed": {
            "past": "What rest was cut short?",
            "present": "What cannot find peace?",
            "future": "What may not rest?"
        }
    },
    "Five of Swords": {
        "upright": {
            "past": "What was won at a cost?",
            "present": "What cuts both ways?",
            "future": "What victory may be hollow?"
        },
        "reversed": {
            "past": "What weapons were laid down?",
            "present": "What conflict softens?",
            "future": "What may be reconciled?"
        }
    },
    "Six of Swords": {
        "upright": {
            "past": "What passage was made?",
            "present": "What is moving away?",
            "future": "What calmer shores await?"
        },
        "reversed": {
            "past": "What was carried along?",
            "present": "What resists the crossing?",
            "future": "What passage may stall?"
        }
    },
    "Seven of Swords": {
        "upright": {
            "past": "What moved unseen?",
            "present": "What is hidden?",
            "future": "What may require stealth?"
        },
        "reversed": {
            "past": "What came to light?",
            "present": "What truth surfaces?",
            "future": "What will be uncovered?"
        }
    },
    "Eight of Swords": {
        "upright": {
            "past": "What felt like a trap?",
            "present": "What binds?",
            "future": "What may ensnare?"
        },
        "reversed": {
            "past": "What opened?",
            "present": "What loosens?",
            "future": "What freedom awaits?"
        }
    },
    "Nine of Swords": {
        "upright": {
            "past": "What haunted?",
            "present": "What circles in the dark?",
            "future": "What may keep sleep away?"
        },
        "reversed": {
            "past": "What loosened its grip?",
            "present": "What eases?",
            "future": "What peace will return?"
        }
    },
    "Ten of Swords": {
        "upright": {
            "past": "What fell completely?",
            "present": "What has reached its end?",
            "future": "What must end?"
        },
        "reversed": {
            "past": "What worst passed?",
            "present": "What is lifting?",
            "future": "What will rise again?"
        }
    },
    "Page of Swords": {
        "upright": {
            "past": "What was discovered?",
            "present": "What demands attention?",
            "future": "What message awaits?"
        },
        "reversed": {
            "past": "What cut carelessly?",
            "present": "What sharp edge threatens?",
            "future": "What words may wound?"
        }
    },
    "Knight of Swords": {
        "upright": {
            "past": "What was charged after?",
            "present": "What rushes forward?",
            "future": "What will demand swift action?"
        },
        "reversed": {
            "past": "What moved too fast?",
            "present": "What lacks direction?",
            "future": "What haste may harm?"
        }
    },
    "Queen of Swords": {
        "upright": {
            "past": "What was cut away cleanly?",
            "present": "What requires clear seeing?",
            "future": "What will need discernment?"
        },
        "reversed": {
            "past": "What grew too sharp?",
            "present": "What cuts too deep?",
            "future": "What coldness may set in?"
        }
    },
    "King of Swords": {
        "upright": {
            "past": "What was decided with clarity?",
            "present": "What sees clearly?",
            "future": "What will be judged fairly?"
        },
        "reversed": {
            "past": "What ruled without heart?",
            "present": "What thinks without feeling?",
            "future": "What may cut too coldly?"
        }
    },

    # === PENTACLES ===
    "Ace of Pentacles": {
        "upright": {
            "past": "What seed took root?",
            "present": "What is being planted?",
            "future": "What will take form?"
        },
        "reversed": {
            "past": "What seed failed?",
            "present": "What struggles to root?",
            "future": "What may not take hold?"
        }
    },
    "Two of Pentacles": {
        "upright": {
            "past": "What was kept in balance?",
            "present": "What is being juggled?",
            "future": "What will need balancing?"
        },
        "reversed": {
            "past": "What tipped over?",
            "present": "What wobbles?",
            "future": "What may be dropped?"
        }
    },
    "Three of Pentacles": {
        "upright": {
            "past": "What was built with care?",
            "present": "What is being crafted?",
            "future": "What will be built?"
        },
        "reversed": {
            "past": "What fell apart in the making?",
            "present": "What lacks solid craft?",
            "future": "What may crumble?"
        }
    },
    "Four of Pentacles": {
        "upright": {
            "past": "What was held tight?",
            "present": "What is being guarded?",
            "future": "What will be secured?"
        },
        "reversed": {
            "past": "What grip loosened?",
            "present": "What is opening?",
            "future": "What will be released?"
        }
    },
    "Five of Pentacles": {
        "upright": {
            "past": "What was weathered?",
            "present": "What feels lacking?",
            "future": "What hardship approaches?"
        },
        "reversed": {
            "past": "What turned around?",
            "present": "What improves?",
            "future": "What relief awaits?"
        }
    },
    "Six of Pentacles": {
        "upright": {
            "past": "What was given or received?",
            "present": "What flows between hands?",
            "future": "What exchange awaits?"
        },
        "reversed": {
            "past": "What came with conditions?",
            "present": "What gives unevenly?",
            "future": "What debt may form?"
        }
    },
    "Seven of Pentacles": {
        "upright": {
            "past": "What grew slowly?",
            "present": "What is ripening?",
            "future": "What harvest approaches?"
        },
        "reversed": {
            "past": "What didn't yield?",
            "present": "What tests patience?",
            "future": "What may not bear fruit?"
        }
    },
    "Eight of Pentacles": {
        "upright": {
            "past": "What was refined through effort?",
            "present": "What is being shaped?",
            "future": "What will be mastered?"
        },
        "reversed": {
            "past": "What lost its purpose?",
            "present": "What effort feels empty?",
            "future": "What may lack care?"
        }
    },
    "Nine of Pentacles": {
        "upright": {
            "past": "What was cultivated alone?",
            "present": "What flourishes?",
            "future": "What abundance awaits?"
        },
        "reversed": {
            "past": "What cost too much?",
            "present": "What feels empty despite fullness?",
            "future": "What may ring hollow?"
        }
    },
    "Ten of Pentacles": {
        "upright": {
            "past": "What was passed down?",
            "present": "What endures?",
            "future": "What will last?"
        },
        "reversed": {
            "past": "What inheritance was troubled?",
            "present": "What foundation shakes?",
            "future": "What may not hold?"
        }
    },
    "Page of Pentacles": {
        "upright": {
            "past": "What seed was planted?",
            "present": "What is being learned?",
            "future": "What opportunity awaits?"
        },
        "reversed": {
            "past": "What never got started?",
            "present": "What lacks follow-through?",
            "future": "What may be wasted?"
        }
    },
    "Knight of Pentacles": {
        "upright": {
            "past": "What was built step by step?",
            "present": "What moves steadily?",
            "future": "What will be earned through patience?"
        },
        "reversed": {
            "past": "What got stuck?",
            "present": "What stagnates?",
            "future": "What may not move?"
        }
    },
    "Queen of Pentacles": {
        "upright": {
            "past": "What was tended with care?",
            "present": "What is nurtured?",
            "future": "What will grow through tending?"
        },
        "reversed": {
            "past": "What was neglected?",
            "present": "What drains?",
            "future": "What may wither?"
        }
    },
    "King of Pentacles": {
        "upright": {
            "past": "What was built to last?",
            "present": "What stands solid?",
            "future": "What will be secured?"
        },
        "reversed": {
            "past": "What crumbled from excess?",
            "present": "What weighs down?",
            "future": "What may be lost to greed?"
        }
    },
}


def get_card_reflection(card_name: str, is_reversed: bool, tense: str = "present") -> str:
    """Get the reflection prompt for a specific card and tense"""
    orientation = "reversed" if is_reversed else "upright"

    if card_name in CARD_REFLECTIONS:
        card_data = CARD_REFLECTIONS[card_name].get(orientation, {})
        return card_data.get(tense, card_data.get("present", "What does this reveal?"))

    return "What does this reveal?"
