"""
phoenix_eye.py
----------------
Detects aura transformations and class-level symbolic shifts based on mana.

Author: Khaylub Thompson-Calvin

Purpose:
    - Interpret symbolic 'mana' and memory tag into aura tiers
    - Trigger class-level changes based on transformation thresholds
    - Feed aura output into transmutation responses or illusions

Symbolic Tiering:
    • Mana < 50: Dormant
    • Mana 50–100: Kindled
    • Mana 100–150: Ascending
    • Mana >150: Phoenix Phase (Class shift trigger)
"""

def detect_aura_shift(mana, memory_tag=None):
    """
    Maps mana value to aura tier and evaluates possible evolution.

    Args:
        mana (int): The symbolic energy computed.
        memory_tag (str): Optional symbolic tag tied to a reflection or event.

    Returns:
        dict: Aura classification and evolution trigger (if any).
    """
    aura_tier = "Dormant"
    class_shift = False

    if mana >= 150:
        aura_tier = "Phoenix Phase"
        class_shift = True
    elif 100 <= mana < 150:
        aura_tier = "Ascending"
    elif 50 <= mana < 100:
        aura_tier = "Kindled"

    return {
        "aura_tier": aura_tier,
        "evolved": class_shift,
        "memory_reference": memory_tag or "none"
    }
