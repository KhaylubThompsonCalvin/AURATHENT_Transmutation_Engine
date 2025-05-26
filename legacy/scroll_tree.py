"""
scroll_tree.py
---------------
Loads scroll evolution logic from scroll_tree.json.

Author: Khaylub Thompson-Calvin

Purpose:
    - Based on user virtue history, return scroll evolution path
    - Reads from symbolic scroll structure stored in JSON
"""

import json
import os

# Absolute path to the scroll_tree.json file
SCROLL_TREE_PATH = os.path.join(os.path.dirname(__file__), "scroll_tree.json")

def load_scroll_data():
    """
    Load scroll path data from scroll_tree.json.

    Returns:
        dict: The loaded JSON data or empty dict on failure.
    """
    try:
        with open(SCROLL_TREE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[scroll_tree] Error loading scroll data: {e}")
        return {}

def get_scroll_path(user_id, virtue):
    """
    Get the scroll evolution path for a user and virtue.

    Args:
        user_id (str): The user's unique identifier.
        virtue (str): The virtue being evolved.

    Returns:
        list: List of scroll path stages.
    """
    scroll_data = load_scroll_data()

    return (
        scroll_data.get(user_id, {}).get(virtue) or
        scroll_data.get("defaults", {}).get(virtue) or
        [f"{virtue}_init", f"{virtue}_path", f"{virtue}_trial"]
    )
