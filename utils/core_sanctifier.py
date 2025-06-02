"""
core_sanctifier.py
-------------------
The central chamber that fuses breath, emotion, and virtue data into a symbolic state.

Author: Khaylub Thompson-Calvin
Date: 2025-05-31

Purpose:
    - Intake breath logs and transmute into perception scores
    - Amplify symbolic purity based on aura and virtue resonance
    - Return sanctified payload for vault scoring or legacy triggers
"""

from datetime import datetime
from utils.mana_converter import convert_experience_to_mana
from utils.phoenix_eye import detect_aura_shift
from utils.lapis_index import trigger_lapis_event
from models.query_log import log_event
from models.transmutation_record import record_transmutation

def sanctify_input(user_id, emotion, virtue, breath_cycle=1, memory_tag=None):
    """
    Converts raw symbolic input into a sanctified core response.

    Args:
        user_id (str): Unique ID of the user
        emotion (str): Emotional state
        virtue (str): Virtue input
        breath_cycle (int): Breath multiplier (focus / awareness)
        memory_tag (str): Optional tag to influence aura evolution

    Returns:
        dict: Sanctified symbolic payload
    """
    try:
        # A) Calculate symbolic mana
        mana = convert_experience_to_mana(emotion, virtue) * breath_cycle

        # B) Detect aura state
        aura_result = detect_aura_shift(mana, memory_tag)

        # C) Trigger divine logic (lapis)
        lapis_triggered = trigger_lapis_event(virtue, memory_tag)

        # D) Record to symbolic transmutation history
        record = record_transmutation(
            user_id,
            emotion,
            virtue,
            mana,
            aura_result["aura_tier"],
            lapis_triggered
        )

        # E) Log it
        log_event("core_sanctifier", {
            "user": user_id,
            "virtue": virtue,
            "emotion": emotion,
            "mana": mana,
            "aura": aura_result,
            "lapis": lapis_triggered
        })

        return {
            "status": "sanctified",
            "timestamp": record["timestamp"],
            "mana": mana,
            "aura_result": aura_result,
            "lapis_triggered": lapis_triggered
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

