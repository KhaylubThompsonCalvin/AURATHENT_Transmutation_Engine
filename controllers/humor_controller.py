# controllers/humor_controller.py

"""
humor_controller.py
-------------------
Analyzes submitted humor as a logical paradox detector.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Receive submitted joke, phrase, or paradox
    - Pass input through the Laughter Filter engine
    - Log authenticity and paradox resolution strength
    - Return a “Humor Index” to aid perception training and symbolic resonance

Symbolic Tie-In:
    - Laughing reflects cognitive transcendence (Davidic Eye Level 5 logic)
    - Humor = abstract acceptance of symbolic duality
"""

from flask import Blueprint, request, jsonify
from utils.laughter_filter import validate_humor_paradox, validate_humor_signal


humor_bp = Blueprint('humor', __name__)

@humor_bp.route('/humor/analyze', methods=['POST'])
def analyze_humor():
    """
    Endpoint: /humor/analyze
    Accepts JSON: { "content": str }
    Returns: {
        "status": "analyzed",
        "original": str,
        "humor_index": float,
        "decoded_meaning": str,
        "paradox_resolved": bool
    }
    """
    try:
        data = request.get_json(force=True)
        content = data.get("content")

        if not content:
            return jsonify({"error": "Missing humor content"}), 400

        # Run the content through the paradox detector
        result = validate_humor_paradox(content)

        return jsonify({
            "status": "analyzed",
            "original": content,
            "humor_index": result.get("humor_index"),
            "decoded_meaning": result.get("meaning"),
            "paradox_resolved": result.get("paradox_resolved")
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500



