"""
emotion_model.py
-----------------
Defines the emotional data structure and symbolic logic relationships
used in emotion logging, memory recall, and perception analysis.

Author: Khaylub Thompson-Calvin

Purpose:
    - Track emotions input by user in symbolic form
    - Record intensity and optional memory association
    - Used in training auric responses and perception streaks
"""

from datetime import datetime

class EmotionEntry:
    def __init__(self, emotion_type, intensity, memory_reference=None):
        """
        Initializes an emotion event.

        Args:
            emotion_type (str): The symbolic name of the emotion (e.g., "sorrow", "hope").
            intensity (int): A numeric score from 1–10 reflecting emotional strength.
            memory_reference (str, optional): Tag or hash for associated memory event.
        """
        self.emotion_type = emotion_type
        self.intensity = intensity
        self.memory_reference = memory_reference
        self.timestamp = datetime.utcnow()

    def to_dict(self):
        """
        Converts the object into a dictionary for JSON or database logging.
        """
        return {
            "emotion": self.emotion_type,
            "intensity": self.intensity,
            "memory": self.memory_reference,
            "timestamp": self.timestamp.isoformat()
        }

