"""
transmutation_record.py
------------------------
Records finalized symbolic transmutations across sessions.

Author: Khaylub Thompson-Calvin
Date: 2025-05-31

Purpose:
    - Store transmutation outcomes linked to user profiles
    - Capture full input/output of each symbolic transformation
    - Enable reflection, sorting, insight unlocking, and memory streaks
"""

from datetime import datetime

# In-memory symbolic log store
transmutation_records = {}


def record_transmutation(user_id, emotion, virtue, mana, aura_result, lapis_triggered):
    """
    Logs a completed transmutation event.

    Args:
        user_id (str): The unique ID of the user
        emotion (str): Triggering emotion
        virtue (str): Contributing virtue
        mana (float): Mana generated from the combination
        aura_result (dict): Full result from detect_aura_shift()
        lapis_triggered (bool): Whether a divine logic trigger was activated

    Returns:
        dict: The stored symbolic transmutation event
    """
    if not user_id:
        raise ValueError("User ID must be provided for transmutation logging.")

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "emotion": emotion,
        "virtue": virtue,
        "mana": round(float(mana), 2),
        "aura_tier": aura_result.get("aura_tier"),
        "class_shift": aura_result.get("evolved"),
        "memory_reference": aura_result.get("memory_reference"),
        "lapis_triggered": lapis_triggered
    }

    if user_id not in transmutation_records:
        transmutation_records[user_id] = []

    transmutation_records[user_id].append(entry)
    return entry


def get_transmutation_history(user_id):
    """
    Retrieves the complete transmutation history for a user.

    Args:
        user_id (str): The user's unique identifier

    Returns:
        list: List of symbolic transformation events
    """
    return transmutation_records.get(user_id, [])


def summarize_transmutations(user_id):
    """
    Generates a readable symbolic timeline of aura shifts.

    Args:
        user_id (str): The user's unique identifier

    Returns:
        list[str]: Summary descriptions of symbolic transitions
    """
    history = get_transmutation_history(user_id)
    return [
        f"{record['timestamp']} → {record['aura_tier']} ({record['virtue']} + {record['emotion']})"
        for record in history
    ]
