# controllers/transmutation_controller.py

"""
transmutation_controller.py
----------------------------
Handles symbolic transmutation input from the user.
Transforms emotional and virtue-based stimuli into aura or symbolic states.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Receive POST requests from frontend or perception UI
    - Validate and log emotion/virtue combo
    - Pass inputs through the symbolic engine (mana + phoenix_eye + lapis_index)
    - Return structured symbolic output (e.g., aura state, illusion level)
"""

from flask import Blueprint, request, jsonify
from utils.mana_converter import convert_experience_to_mana
from utils.phoenix_eye import detect_aura_shift
from utils.lapis_index import trigger_lapis_event

transmutation_bp = Blueprint('transmutation', __name__)

@transmutation_bp.route('/transmute', methods=['POST'])
def transmute():
    """
    Endpoint: /transmute
    Accepts JSON: { "emotion": str, "virtue": str, "memory": optional str }
    Returns: {
        "status": "success",
        "mana": float,
        "aura_result": dict,
        "lapis_triggered": dict
    }
    """
    try:
        data = request.get_json(force=True)
        emotion = data.get('emotion')
        virtue  = data.get('virtue')
        memory_tag = data.get('memory')

        if not emotion or not virtue:
            return jsonify({"error": "Missing emotion or virtue input"}), 400

        # 1) Convert raw inputs into a mana score
        mana = convert_experience_to_mana(emotion, virtue)

        # 2) Detect any shift in aura based on mana + memory context
        aura_result = detect_aura_shift(mana, memory_tag)

        # 3) Possibly trigger a divine (lapis) event from virtue + memory
        divine_trigger = trigger_lapis_event(virtue, memory_tag)

        return jsonify({
            "status": "success",
            "mana": mana,
            "aura_result": aura_result,
            "lapis_triggered": divine_trigger
        }), 200

    except Exception as e:
        # Catch-all for unexpected failures
        return jsonify({"error": str(e)}), 500

