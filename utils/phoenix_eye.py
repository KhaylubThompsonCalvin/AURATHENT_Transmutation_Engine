"""
phoenix_eye.py
----------------
Detects aura transformations and class-level symbolic shifts based on mana.

Author: Khaylub Thompson-Calvin

Purpose:
    - Interpret symbolic 'mana' and memory tag into aura tiers
    - Trigger class-level changes based on transformation thresholds
    - Feed aura output into transmutation responses or illusions
    - Return numeric tier scores for sorting or evolution thresholds

Symbolic Tiering:
    • Mana < 50: Dormant
    • Mana 50–99: Kindled
    • Mana 100–149: Ascending
    • Mana ≥ 150: Phoenix Phase (Class shift trigger)
"""

from models.query_log import log_event

def detect_aura_shift(mana, memory_tag=None):
    """
    Maps mana value to aura tier and evaluates possible evolution.

    Args:
        mana (int): The symbolic energy computed.
        memory_tag (str): Optional symbolic tag tied to a reflection or event.

    Returns:
        dict: Aura classification, evolution flag, and reference.
    """
    aura_tier = "Dormant"
    tier_score = 0
    class_shift = False

    if mana >= 150:
        aura_tier = "Phoenix Phase"
        tier_score = 3
        class_shift = True
    elif 100 <= mana < 150:
        aura_tier = "Ascending"
        tier_score = 2
    elif 50 <= mana < 100:
        aura_tier = "Kindled"
        tier_score = 1

    result = {
        "aura_tier": aura_tier,
        "tier_score": tier_score,
        "evolved": class_shift,
        "memory_reference": memory_tag or "none"
    }

    # Optional: log symbolic aura detection for audit trail
    log_event("phoenix_eye", {
        "mana": mana,
        "tier": aura_tier,
        "score": tier_score,
        "evolved": class_shift,
        "memory_tag": memory_tag or "none"
    })

    return result
