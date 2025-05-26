"""
laughter_filter.py
-------------------
Processes symbolic humor input and determines authenticity of laughter.
Used in social, emotional, and illusion-based decoding layers.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Analyze the structure and context of a humor input
    - Detect whether humor is an authentic expression or coping mask
    - Detect paradoxes that reflect abstract symbolic insight
    - Feed output into symbolic memory or aura transmutation

Symbolic Classes:
    • Authentic → Insight, bonding, light-based mana
    • Hollow → Misdirection, shadow masking, paradox source
    • Paradox → Layered cognitive resonance (Davidic Eye Logic)
"""

import random

# -------------------------------------------------------------------
# Humor Authenticity Signal
# -------------------------------------------------------------------
def validate_humor_signal(joke_text, emotion_context):
    """
    Analyzes a humor signal for authenticity based on structure and emotion.

    Args:
        joke_text (str): The joke or humorous phrase.
        emotion_context (str): The dominant emotional state of the user.

    Returns:
        dict: Symbolic evaluation result.
    """
    humor_length = len(joke_text.strip())
    has_irony = "not" in joke_text.lower() or "unless" in joke_text.lower()
    emotional_alignment = emotion_context.lower() in ["joy", "surprise", "relief"]

    score = 0
    if humor_length > 20:
        score += 1
    if has_irony:
        score += 1
    if emotional_alignment:
        score += 2

    if score >= 3:
        quality = "authentic"
        essence = "clarity-signal"
    else:
        quality = "hollow"
        essence = "masking-echo"

    return {
        "humor_quality": quality,
        "symbolic_essence": essence,
        "score": score
    }

# -------------------------------------------------------------------
# Humor Paradox Analyzer (Symbolic Layer)
# -------------------------------------------------------------------
def validate_humor_paradox(content):
    """
    Detects paradox and duality layers in a humor input for symbolic scoring.

    Args:
        content (str): The joke, paradox, or humorous input.

    Returns:
        dict: {
            "humor_index": float,
            "meaning": str,
            "paradox_resolved": bool
        }
    """
    keywords = ["why", "because", "walks into", "knock", "loop", "absurd", "existential"]
    duality_found = any(k in content.lower() for k in keywords)

    if "because" in content.lower():
        meaning = "The logic explains itself—mirroring causality."
    elif "walks into" in content.lower():
        meaning = "Physical meets symbolic; humor from displacement."
    elif "knock" in content.lower():
        meaning = "Threshold logic—question becomes door."
    elif "loop" in content.lower():
        meaning = "Circular paradox—humor from self-reference."
    elif "existential" in content.lower():
        meaning = "The joke probes the void with a grin."
    else:
        meaning = "This joke dances at the edge of contradiction."

    return {
        "humor_index": round(random.uniform(0.5, 0.95) if duality_found else random.uniform(0.1, 0.4), 2),
        "meaning": meaning,
        "paradox_resolved": duality_found
    }
