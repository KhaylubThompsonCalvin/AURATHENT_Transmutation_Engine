"""
app.py
-------
Main entry point for the AURATHENT Transmutation Engine.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Bootstraps the Flask symbolic transmutation backend engine.
    - Loads environment variables from .env (secrets, DB credentials, port).
    - Initializes MongoDB (via PyMongo) and PostgreSQL connection pool.
    - Registers all controller Blueprints for:
        • Symbolic transmutation
        • Virtue vessel updates
        • Emotion logging
        • Memory anchoring
        • Humor analysis
        • Central logic routing
        • Breath logging (this new endpoint)
        • (Optional) OpenAI agent services
    - Exposes a health-check endpoint.
    - Launches the aura-based symbolic routing gateway on configured port.

Dependencies:
    flask, flask-cors, python-dotenv, flask-pymongo, psycopg2, openai
"""

import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Import the breath_controller blueprint
from controllers.breath_controller import breath_bp

# Load environment variables from .env
load_dotenv()

# ------------------------------------------------------------------
# Database connection setup
# ------------------------------------------------------------------
from database import (
    init_mongo,
    init_postgres_pool,
    get_postgres_connection,
    release_postgres_connection
)

# ------------------------------------------------------------------
# Import other controller blueprints
# ------------------------------------------------------------------
from controllers.transmutation_controller import transmutation_bp
from controllers.virtue_vessel_controller import virtue_vessel_bp
from controllers.emotion_controller import emotion_bp
from controllers.memory_controller import memory_bp
from controllers.humor_controller import humor_bp
from controllers.logic_router import logic_bp

# ------------------------------------------------------------------
# Optional: OpenAI Blueprint
# ------------------------------------------------------------------
OPENAI_ENABLED = False
try:
    from controllers.openai_controller import openai_bp
    OPENAI_ENABLED = True
except ImportError as e:
    print(f"[OpenAI] Controller not loaded: {e}")


def create_app():
    """
    Creates the Flask app with CORS, Mongo/Postgres, and API routes.
    """
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "aurathent-core-spark")

    # Initialize databases
    init_mongo(app)
    init_postgres_pool(minconn=2, maxconn=10, app=app)

    # Register all API endpoints
    app.register_blueprint(transmutation_bp, url_prefix="/api/transmute")
    app.register_blueprint(virtue_vessel_bp, url_prefix="/api/virtue")
    app.register_blueprint(emotion_bp, url_prefix="/api/emotion")
    app.register_blueprint(memory_bp, url_prefix="/api/memory")
    app.register_blueprint(humor_bp, url_prefix="/api/humor")
    app.register_blueprint(logic_bp, url_prefix="/api/logic")

    # Register the breath blueprint at /api/breath
    app.register_blueprint(breath_bp, url_prefix="/api/breath")

    if OPENAI_ENABLED:
        app.register_blueprint(openai_bp, url_prefix="/api/openai")

    # Root health check
    @app.route("/", methods=["GET"])
    def health():
        return {
            "status": "online",
            "message": "AURATHENT Transmutation Engine Active",
            "openai": "enabled" if OPENAI_ENABLED else "disabled"
        }, 200

    return app


if __name__ == "__main__":
    try:
        conn = get_postgres_connection()
        if conn:
            print("[PostgreSQL] Connection verified.")
            release_postgres_connection(conn)
    except Exception as e:
        print(f"[PostgreSQL] Startup connection check failed: {e}")

    # Run the Flask server
    app = create_app()
    port = int(os.getenv("PORT", 5001))
    print(f"[Flask] Launching on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)
