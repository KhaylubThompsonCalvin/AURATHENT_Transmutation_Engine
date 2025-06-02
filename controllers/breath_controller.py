# controllers/breath_controller.py
# ---------------------
# Handles symbolic breath log inputs and routes them through the Sanctified Core.

from flask import Blueprint, request, jsonify
from datetime import datetime
from utils.core_sanctifier import sanctify_input

breath_bp = Blueprint('breath', __name__)

@breath_bp.route('/log', methods=['POST'])
def breath_log():
    """
    POST /api/breath/log

    Payload Example:
        {
            "user_id": "alpha01",
            "emotion": "awe",
            "virtue": "truth",
            "breath_cycle": 2,
            "memory_tag": "reflection"
        }

    Returns:
        {
            "status": "sanctified",
            "timestamp": "...",
            "mana": int,
            "aura_result": { ... },
            "lapis_triggered": bool
        }
    """
    try:
        data = request.get_json(force=True)

        user_id = data.get("user_id", "default_user")
        emotion = data.get("emotion")
        virtue = data.get("virtue")
        breath_cycle = data.get("breath_cycle", 1)
        memory_tag = data.get("memory_tag", None)

        if not emotion or not virtue:
            return jsonify({
                "status": "error",
                "message": "Missing 'emotion' or 'virtue' in payload."
            }), 400

        # Call sanctify_input and handle both string and dict results
        result = sanctify_input(user_id, emotion, virtue, breath_cycle, memory_tag)

        if isinstance(result, dict):
            result["status"] = "sanctified"
            result["timestamp"] = datetime.utcnow().isoformat()
            return jsonify(result), 200
        else:
            # result is a string or other non-dict output
            return jsonify({
                "status": "sanctified",
                "message": str(result),
                "timestamp": datetime.utcnow().isoformat()
            }), 200

    except Exception as e:
        print(f"[ERROR] breath_log() :: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500



