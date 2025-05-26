# controllers/emotion_controller.py

"""
emotion_controller.py
---------------------
Captures raw emotional states and processes them into symbolic weights.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Accept POST requests from the emotional UI sensors or symbolic logs
    - Validate emotional input types (e.g., joy, fear, awe, guilt)
    - Convert emotion into intensity weight for memory mapping and transmutation
    - Log emotional weights for symbolic timing via ChronoSynth
    - Render symbolic emotion states via Jinja (for prototype testing)
"""

from flask import Blueprint, request, jsonify, render_template
from utils.chrono_synth import log_emotion_event

emotion_bp = Blueprint('emotion', __name__)

@emotion_bp.route('/log', methods=['POST'])
def log_emotion():
    """
    POST /api/emotion/log
    Payload:
        {
            "emotion": "joy",
            "intensity": 1.5
        }
    Returns:
        {
            "status": "logged",
            "emotion": "joy",
            "intensity": 1.5,
            "chrono_reference": "2025-05-25T12:34:56"
        }
    """
    try:
        data = request.get_json(force=True)
        emotion = data.get('emotion')
        intensity = data.get('intensity', 1.0)

        if not emotion:
            return jsonify({"error": "Missing emotion type"}), 400

        log_result = log_emotion_event(emotion, intensity)

        return jsonify({
            "status": "logged",
            "emotion": emotion,
            "intensity": intensity,
            "chrono_reference": log_result.get("timestamp")
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@emotion_bp.route('/view', methods=['GET'])  # ✅ clean endpoint
def emotion_view():
    """
    GET /api/emotion/view
    Renders a test template using sample emotional data.
    """
    emotions = [
        {"name": "joy", "level": 2},
        {"name": "awe", "level": 4}
    ]
    return render_template("virtue_display.html", virtues=emotions)

