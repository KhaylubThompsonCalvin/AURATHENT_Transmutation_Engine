"""
izumi_izanagi_gate.py
----------------------
Symbolically transmutes paradox into encoded symbolic fire (transcendence state).

Author: Khaylub Thompson-Calvin

Purpose:
    - Analyze emotional/virtue paradoxes to detect high-impact symbolic events
    - Output narrative-coded "flames" based on energetic strain and internal contradiction
    - Resolve paradox chains for symbolic analysis and class evaluation
"""

# -----------------------------------------------
# Evaluate symbolic paradox strength
# -----------------------------------------------
def evaluate_paradox(emotion, virtue):
    """
    Determine whether the input pair creates a symbolic paradox.

    Args:
        emotion (str): Emotional input (e.g., fear, pride)
        virtue (str): Virtue input (e.g., courage, humility)

    Returns:
        tuple: (paradox_level: int, flame_name: str)
    """
    paradox_pairs = {
        ("fear", "courage"): (5, "Black Flame of Insight"),
        ("anger", "forgiveness"): (4, "Crimson Wreath"),
        ("grief", "joy"): (3, "Ashen Blossom"),
        ("envy", "gratitude"): (4, "Emerald Flicker"),
        ("pride", "humility"): (5, "Ivory Fire")
    }

    key = (emotion.lower(), virtue.lower())
    reversed_key = (virtue.lower(), emotion.lower())

    return paradox_pairs.get(key) or paradox_pairs.get(reversed_key) or (1, "Dim Spark")

# -----------------------------------------------
# Resolve paradox and return symbolic structure
# -----------------------------------------------
def resolve_paradox_chain(virtue, emotion):
    """
    Resolves symbolic paradoxes between virtues and emotions
    to generate high-impact transformation phrases.

    Args:
        virtue (str): The symbolic virtue involved (e.g., humility, courage)
        emotion (str): The conflicting or complementing emotion (e.g., fear, pride)

    Returns:
        dict: {
            "level": int,
            "flame": str,
            "paradox": bool,
            "description": str
        }
    """
    fire_level, flame = evaluate_paradox(emotion, virtue)

    paradox_map = {
        ("compassion", "anger"): "Forgiveness inside rage births growth.",
        ("truth", "fear"): "Courage to reveal what is hidden.",
        ("wisdom", "grief"): "Loss is the tutor of insight.",
        ("honor", "shame"): "Integrity tested by failure yields purity.",
        ("fear", "courage"): "Fear faced with courage creates transformation.",
        ("pride", "humility"): "Pride restrained by humility reveals divinity.",
        ("envy", "gratitude"): "Gratitude dissolves the green fog of envy."
    }

    key = (virtue.lower(), emotion.lower())
    reversed_key = (emotion.lower(), virtue.lower())

    symbolic_description = paradox_map.get(key) or paradox_map.get(reversed_key) or (
        f"No paradox detected between {virtue} and {emotion}."
    )

    return {
        "level": fire_level,
        "flame": flame,
        "paradox": fire_level > 1,
        "description": symbolic_description
    }

