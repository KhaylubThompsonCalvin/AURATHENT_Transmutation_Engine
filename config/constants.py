# config/constants.py
"""
constants.py
------------
Defines symbolic thresholds, virtue weights, and KI amplification scales.

Author: Khaylub Thompson‐Calvin
Date: 2025‐05‐25 (updated 2025-06-01)
"""

# Core thresholds for virtue resonance (new virtues added)
VIRTUE_THRESHOLDS = {
    "wisdom":      7,
    "honor":       8,
    "compassion":  5,
    "truth":      10,
    "resilience":  6,
    "sacrifice":   9,   # new
    "insight":     8,   # new
    "reverence":   7    # new
}

# KI‐based amplification rates (no changes unless you added levels)
KI_AMPLIFIER = {
    "low":       1.00,
    "moderate":  1.50,
    "high":      2.25,
    # "legendary": 3.50  # uncomment if you introduce a new tier
}

# Symbolic purity reference for aura states (must match detect_aura_shift tiers)
AURA_STATES = [
    "Dormant",
    "Kindled",
    "Ascending",
    "Phoenix Phase"
]

# (If you still need the old “fog→echo→clarity→illumination” for legacy reasons,
#  put them in a separate constant, e.g. LEGACY_AURA_STATES = ["fog","echo","clarity","illumination"].)
