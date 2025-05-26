"""
aura_model.py
--------------
Handles the transformation of user aura states and symbolic class-level evolution.

Author: Khaylub Thompson-Calvin

Purpose:
    - Interpret mana levels and virtue inputs into aura changes
    - Track symbolic aura states (e.g., lumina, void, prism, eclipse)
    - Trigger class evolution based on aura shifts and scroll history

Aura States (Examples):
    - "neutral": Base state
    - "lumina": Light-bound clarity (high harmony + hope)
    - "void": Emotional numbness (excess paradox)
    - "prism": Reflective growth (diverse virtue engagement)
    - "eclipse": Transformation under pressure (high mana + contradiction)
"""

aura_registry = {}

def initialize_aura(user_id):
    if user_id not in aura_registry:
        aura_registry[user_id] = {
            "current": "neutral",
            "history": []
        }

def update_aura(user_id, new_state):
    initialize_aura(user_id)
    aura_registry[user_id]["history"].append(aura_registry[user_id]["current"])
    aura_registry[user_id]["current"] = new_state

def get_current_aura(user_id):
    return aura_registry.get(user_id, {}).get("current", "neutral")

def get_aura_history(user_id):
    return aura_registry.get(user_id, {}).get("history", [])

def infer_aura(mana_level, virtue, modifiers=None):
    """
    Simple symbolic engine to infer aura state from mana and virtue input.
    """
    if mana_level > 90 and virtue == "hope":
        return "lumina"
    elif mana_level > 75 and virtue == "truth":
        return "prism"
    elif mana_level > 60 and virtue == "resolve":
        return "eclipse"
    elif mana_level < 20 and virtue == "detachment":
        return "void"
    else:
        return "neutral"
