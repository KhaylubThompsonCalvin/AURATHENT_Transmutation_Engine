"""
mana_converter.py
------------------
Converts emotional and virtue inputs into symbolic 'mana' units
used by downstream transmutation logic.

Author: Khaylub Thompson-Calvin

Purpose:
    - Weigh emotion and virtue synergy
    - Normalize scores into symbolic energy outputs
    - Prepare symbolic payload for aura shift or paradox ignition
"""

def convert_experience_to_mana(emotion, virtue):
    """
    Converts emotional and virtue input into a symbolic mana value.

    Args:
        emotion (str): The emotional state (e.g., "sorrow", "hope").
        virtue (str): The aligned virtue (e.g., "fortitude", "honesty").

    Returns:
        int: The calculated mana score.
    """
    emotion_weight = len(emotion) * 3
    virtue_weight = len(virtue) * 5
    synergy_bonus = 10 if emotion[0].lower() == virtue[0].lower() else 0

    mana = emotion_weight + virtue_weight + synergy_bonus
    return mana
