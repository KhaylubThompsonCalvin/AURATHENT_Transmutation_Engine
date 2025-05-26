"""
chrono_synth.py
----------------
Generates symbolic timestamps for emotional and memory-based sequences.
Acts as the system’s symbolic pulse, measuring timing between events.

Author: Khaylub Thompson-Calvin

Purpose:
    - Capture the current timestamp during emotional log events
    - Calculate symbolic loops or intervals
    - Store rhythm-based logic for future evolution phases

Symbolic Logic:
    • Short loops imply rapid emotional cycles (Reactive)
    • Long loops imply deeper reflection (Contemplative)
"""

import time
from datetime import datetime

memory_log = []

def log_emotion_event(emotion, intensity):
    """
    Records a timestamped emotional event.

    Args:
        emotion (str): Type of emotion (e.g., awe, fear, joy)
        intensity (int): Numeric value of intensity

    Returns:
        dict: A symbolic memory event with timestamp and values
    """
    now = datetime.utcnow().isoformat()
    entry = {
        "timestamp": now,
        "emotion": emotion,
        "intensity": intensity
    }
    memory_log.append(entry)
    return entry

def calculate_loop_interval():
    """
    Calculates time delta between the last two emotional entries.

    Returns:
        float: Seconds between entries, or -1 if not enough data.
    """
    if len(memory_log) < 2:
        return -1

    t1 = datetime.fromisoformat(memory_log[-2]["timestamp"])
    t2 = datetime.fromisoformat(memory_log[-1]["timestamp"])
    return (t2 - t1).total_seconds()

def process_memory_input(event_type, tags, emotion, intensity, insight=None):
    """
    Anchors a symbolic memory event into the timeline.

    Args:
        event_type (str): e.g., 'reflection', 'encounter', 'trial'
        tags (list): Keyword identifiers
        emotion (str): Emotion associated with the memory
        intensity (int or float): Intensity of the memory event
        insight (str, optional): Reflection or decoded symbolic meaning

    Returns:
        dict: Harmonized timeline reference for memory evolution
    """
    now = datetime.utcnow().isoformat()
    memory_event = {
        "timestamp": now,
        "type": event_type,
        "tags": tags,
        "emotion": emotion,
        "intensity": intensity,
        "insight": insight
    }

    memory_log.append(memory_event)

    return {
        "status": "anchored",
        "timestamp": now,
        "tags": tags,
        "insight": insight
    }

