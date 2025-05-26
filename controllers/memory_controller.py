# controllers/memory_controller.py

"""
memory_controller.py
--------------------
Handles symbolic memory input and timeline anchoring from perception or log-based events.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Accept emotional memory logs (e.g., moment tags, insight logs)
    - Pass through ChronoSynth to sync memory into symbolic timeline
    - Optionally trigger memory echoes if thresholds are crossed
"""

from flask import Blueprint, request, jsonify
from utils.chrono_synth import process_memory_input
from models.symbolic_memory import save_memory_log

memory_bp = Blueprint('memory', __name__)

@memory_bp.route('/memory/log', methods=['POST'])
def log_memory():
    """
    Endpoint: /memory/log
    Accepts JSON:
        {
          "event_type": str,
          "tags": [str, ...],
          "emotion": optional str,
          "intensity": optional float,
          "insight": optional str
        }
    Returns: {
        "status": "success",
        "memory_event": str,
        "chrono_sync": dict
    }
    """
    try:
        data = request.get_json(force=True)
        event_type = data.get('event_type')
        tags       = data.get('tags', [])
        emotion    = data.get('emotion', '')
        intensity  = data.get('intensity', 1.0)
        insight    = data.get('insight')

        if not event_type or not tags:
            return jsonify({"error": "Missing required memory event fields"}), 400

        # 1) Sync into ChronoSynth timeline
        chrono_result = process_memory_input(
            event_type, tags, emotion, intensity, insight
        )

        # 2) Persist into our symbolic memory store
        save_memory_log(
            event_type, tags, emotion, intensity, insight, chrono_result
        )

        return jsonify({
            "status": "success",
            "memory_event": event_type,
            "chrono_sync": chrono_result
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


