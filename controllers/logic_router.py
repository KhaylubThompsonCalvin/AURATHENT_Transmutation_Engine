# controllers/logic_router.py

"""
logic_router.py
----------------
Central decision engine delegating symbolic input logic.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Routes combined inputs (virtue + emotion + memory tags)
      to the appropriate transformation or insight modules.
    - Returns a unified symbolic output object.
"""

from flask import Blueprint, request, jsonify
from utils.mana_converter import convert_experience_to_mana
from utils.phoenix_eye import detect_aura_shift
from utils.izumi_izanagi_gate import resolve_paradox_chain
from utils.wheat_binder import bind_hope_chain  # <--- matches actual function name
from models.query_log import log_query

logic_bp = Blueprint('logic', __name__)

@logic_bp.route('/logic/process', methods=['POST'])
def process_logic_flow():
    """
    Endpoint: /logic/process
    Accepts JSON:
        {
            "virtue": str,
            "emotion": str,
            "memory": optional str
        }
    Returns:
        {
            "mana": float,
            "aura_result": dict,
            "insight": dict,
            "memory_binding": dict,
            "status": str
        }
    """
    try:
        data = request.get_json(force=True)
        virtue = data.get('virtue')
        emotion = data.get('emotion')
        memory_tag = data.get('memory', 'default')

        if not virtue or not emotion:
            return jsonify({"error": "Missing virtue or emotion input"}), 400

        # A) Transmute into symbolic mana
        mana = convert_experience_to_mana(emotion, virtue)

        # B) Analyze aura shift
        aura_result = detect_aura_shift(mana, memory_tag)

        # C) Detect paradox (Izanagi/Izanami layer)
        insight = resolve_paradox_chain(virtue, emotion)

        # D) Attempt to bind hope (Wheat logic)
        memory_binding = bind_hope_chain(emotion, virtue, fatigue_level=3)

        # E) Log everything to the system memory
        log_query(
            user_id="default_user",
            event_type="logic_process",
            payload={
                "virtue": virtue,
                "emotion": emotion,
                "memory_tag": memory_tag,
                "aura": aura_result
            }
        )

        return jsonify({
            "mana": mana,
            "aura_result": aura_result,
            "insight": insight,
            "memory_binding": memory_binding,
            "status": "symbolic_processing_complete"
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
