"""
lapis_index.py
---------------
Triggers a divine insight event when specific symbolic inputs align with ancient logic markers.

Author: Khaylub Thompson-Calvin

Purpose:
    - Evaluate emotion/virtue pairings to see if they match rare lapis-aligned triggers
    - Activate spiritual event logic or philosophical milestone thresholds
    - Used in symbolic memory and perception milestones
"""

from models.query_log import log_event

def trigger_lapis_event(virtue, memory_tag=None):
    """
    Check if virtue aligns with symbolic 'lapis logic' insight triggers.

    Args:
        virtue (str): The core virtue submitted.
        memory_tag (str): Optional memory/context to strengthen the symbolic correlation.

    Returns:
        dict: Details of whether lapis logic was triggered and why.
    """

    lapis_virtues = {"truth", "sacrifice", "wisdom", "insight", "reverence"}
    amplified_contexts = {"death", "destiny", "origin", "betrayal", "childhood"}

    virtue_hit = virtue.lower() in lapis_virtues
    memory_hit = memory_tag and memory_tag.lower() in amplified_contexts

    triggered = virtue_hit or (virtue_hit and memory_hit)

    result = {
        "triggered": triggered,
        "virtue_match": virtue_hit,
        "amplified_context": memory_hit,
        "virtue": virtue,
        "memory_tag": memory_tag or "none"
    }

    log_event("lapis_index", result)
    return result