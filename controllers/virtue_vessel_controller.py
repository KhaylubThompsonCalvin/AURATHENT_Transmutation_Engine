# controllers/virtue_vessel_controller.py

"""
virtue_vessel_controller.py
----------------------------
Handles user-submitted virtue interactions and vessel evolution.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Receives POST input representing a user's chosen virtue
    - Updates symbolic virtue vessel for the user (growth, rank, aura)
    - Triggers evolutionary class state if thresholds crossed
    - Interfaces with legacy scroll tree to guide next steps
"""

from flask import Blueprint, request, jsonify
from models.virtue_profile import update_virtue_affinity
from utils.phoenix_eye import detect_aura_shift
from legacy.scroll_tree import get_scroll_path

virtue_vessel_bp = Blueprint('virtue_vessel', __name__)

@virtue_vessel_bp.route('/virtue/update', methods=['POST'])
def update_vessel():
    """
    Endpoint: /virtue/update
    Accepts JSON: { "user_id": str, "virtue": str }
    Returns: {
        "status": "vessel_updated",
        "updated_profile": dict,
        "aura": dict,
        "scroll_path": list
    }
    """
    try:
        data    = request.get_json(force=True)
        user_id = data.get('user_id')
        virtue  = data.get('virtue')

        if not user_id or not virtue:
            return jsonify({"error": "Missing user_id or virtue"}), 400

        # 1) Grow or rank the user's virtue affinity
        new_profile = update_virtue_affinity(user_id, virtue)

        # 2) Re-evaluate their aura given updated score
        aura = detect_aura_shift(new_profile['score'], virtue)

        # 3) Determine next scroll/tree evolution
        scroll_path = get_scroll_path(user_id, virtue)

        return jsonify({
            "status": "vessel_updated",
            "updated_profile": new_profile,
            "aura": aura,
            "scroll_path": scroll_path
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

