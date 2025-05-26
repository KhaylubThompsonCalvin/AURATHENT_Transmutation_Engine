"""
openai_controller.py
---------------------
Handles interaction with the OpenAI API for symbolic prompts and reflection.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Accept user prompts (symbolic, emotional, philosophical, etc.)
    - Forward them to OpenAI for completion
    - Return the structured response for rendering or insight logging
"""

from flask import Blueprint, request, jsonify
from openai import OpenAI
import os

# Initialize Blueprint
openai_bp = Blueprint('openai', __name__)

# Use OpenAI client with key from environment
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

@openai_bp.route('/echo', methods=['POST'])
def openai_echo():
    """
    POST /api/openai/echo
    Payload:
        {
            "prompt": "What is awe?"
        }
    Returns:
        {
            "status": "ok",
            "prompt": "What is awe?",
            "response": "Awe is the feeling of..."
        }
    """
    try:
        data = request.get_json(force=True)
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Missing prompt."}), 400

        # Generate completion (OpenAI v1+ syntax)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{ "role": "user", "content": prompt }],
            temperature=0.7,
            max_tokens=200
        )

        reply = completion.choices[0].message.content

        return jsonify({
            "status": "ok",
            "prompt": prompt,
            "response": reply
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
