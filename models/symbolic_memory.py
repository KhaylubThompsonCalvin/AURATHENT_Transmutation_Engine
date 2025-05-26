"""
symbolic_memory.py
-------------------
Stores symbolic memory fragments tied to virtue and emotional context.

Author: Khaylub Thompson-Calvin

Purpose:
    - Preserve user memory triggers that affect aura or virtue shift
    - Enable lookup of related fragments during transmutation
    - Provide symbolic insight feedback across user sessions

Structure:
    memory_store = {
        "user_id": [
            {
                "emotion": "awe",
                "virtue": "humility",
                "note": "He kneeled before the enemy",
                "timestamp": "2025-05-25T10:10:10"
            },
            ...
        ]
    }
"""

from datetime import datetime

# In-memory database (for future persistent DB migration)
memory_store = {}

def store_memory(user_id, emotion, virtue, note=""):
    if user_id not in memory_store:
        memory_store[user_id] = []

    memory_store[user_id].append({
        "emotion": emotion,
        "virtue": virtue,
        "note": note,
        "timestamp": datetime.utcnow().isoformat()
    })
    return True

def fetch_recent_memories(user_id, limit=5):
    memories = memory_store.get(user_id, [])
    return sorted(memories, key=lambda x: x["timestamp"], reverse=True)[:limit]

def fetch_by_emotion_virtue(user_id, emotion=None, virtue=None):
    if user_id not in memory_store:
        return []

    return [
        m for m in memory_store[user_id]
        if (emotion is None or m["emotion"] == emotion) and
           (virtue is None or m["virtue"] == virtue)
    ]

def save_memory_log(event_type, tags, emotion, intensity, insight, chrono_result):
    """
    Stores a symbolic memory log using chrono reference and stores in memory_store.

    Args:
        event_type (str): Type of the memory (e.g., 'reflection', 'trial')
        tags (list): Descriptive tags for the event
        emotion (str): Emotional anchor
        intensity (float): Strength of the emotion
        insight (str): Optional reflection text
        chrono_result (dict): Result from ChronoSynth containing 'timestamp'

    Returns:
        dict: The stored memory log entry
    """
    user_id = "default_user"  # Placeholder; use actual user_id if available
    note = insight or f"{event_type} with emotion {emotion} and tags {tags}"

    memory_entry = {
        "emotion": emotion,
        "virtue": tags[0] if tags else "unknown",
        "note": note,
        "intensity": intensity,
        "event_type": event_type,
        "timestamp": chrono_result.get("timestamp")
    }

    if user_id not in memory_store:
        memory_store[user_id] = []

    memory_store[user_id].append(memory_entry)
    return memory_entry
