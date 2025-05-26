"""
virtue_profile.py
------------------
Tracks user virtues, symbolic rank, and their growth across sessions.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Initialize and update user's symbolic virtue stats
    - Support aura evolution based on repeated virtue patterns
    - Interface with scroll_tree.json and vault_key_registry.json for Order alignment

Example Output:
    {
        "user_id": "alpha01",
        "virtues": {
            "courage": 3,
            "patience": 5,
            "clarity": 2
        },
        "last_updated": "2025-05-25T11:11:11"
    }
"""

from datetime import datetime
from models.query_log import log_event

# -----------------------------------------------------------------------------
# In-memory virtue store (replace with DB access later)
# -----------------------------------------------------------------------------
user_profiles = {}


def init_virtue_profile(user_id):
    """
    Initializes a new virtue profile for a given user.
    """
    profile = {
        "user_id": user_id,
        "virtues": {},
        "last_updated": datetime.utcnow().isoformat()
    }
    user_profiles[user_id] = profile
    return profile


def update_virtue(user_id, virtue):
    """
    Increments the specified virtue for the user.
    Logs the update event.

    Args:
        user_id (str): User’s unique ID
        virtue (str): Name of the virtue (e.g., "honor", "resilience")

    Returns:
        int: New virtue level
    """
    if user_id not in user_profiles:
        init_virtue_profile(user_id)

    virtues = user_profiles[user_id]["virtues"]
    virtues[virtue] = virtues.get(virtue, 0) + 1
    user_profiles[user_id]["last_updated"] = datetime.utcnow().isoformat()

    log_event("virtue_update", {
        "user": user_id,
        "virtue": virtue,
        "new_level": virtues[virtue]
    })

    return virtues[virtue]


def get_virtue_profile(user_id):
    """
    Retrieves the user's virtue profile or creates one if absent.

    Args:
        user_id (str): Unique identifier

    Returns:
        dict: Full virtue profile
    """
    return user_profiles.get(user_id, init_virtue_profile(user_id))


def update_virtue_affinity(user_id, virtue):
    """
    Main interface for external modules (controllers).
    Updates the user's virtue, calculates total symbolic score,
    and returns a full profile snapshot.

    Args:
        user_id (str): The user's ID
        virtue (str): The name of the virtue to update

    Returns:
        dict: Structured profile data including total score
    """
    level = update_virtue(user_id, virtue)
    profile = get_virtue_profile(user_id)
    total_score = sum(profile["virtues"].values())

    return {
        "user_id": user_id,
        "virtues": profile["virtues"],
        "score": total_score,
        "last_updated": profile["last_updated"]
    }

