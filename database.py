"""
database.py
------------
Handles database connections for both MongoDB (NoSQL) and PostgreSQL (Relational).

Author: Khaylub Thompson-Calvin (updated)
Purpose:
    - Load credentials from environment (.env)
    - Initialize MongoDB for symbolic/emotion documents
    - Provide a Postgres connection pool for legacy logs and user data
"""

import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool

# Load .env from project root
load_dotenv()

# -----------------------------------------------------------------------------
# MongoDB (Symbolic Document Store)
# -----------------------------------------------------------------------------
mongo = PyMongo()

def init_mongo(app):
    """
    Attach PyMongo to our Flask app.
    Call this from create_app() before registering blueprints.
    """
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/cloeila_dev")
    mongo.init_app(app)

def get_mongo():
    """
    Returns the PyMongo client for direct access:
      from database import get_mongo
      db = get_mongo().db
    """
    return mongo

# -----------------------------------------------------------------------------
# PostgreSQL (Structured Logs / Users) with Connection Pool
# -----------------------------------------------------------------------------
_pg_pool: ThreadedConnectionPool = None

def init_postgres_pool(minconn: int = 1, maxconn: int = 10, app=None):
    """
    Initializes a threaded connection pool for PostgreSQL.
    Call this once at app startup (e.g. in create_app()).
    """
    global _pg_pool
    try:
        _pg_pool = ThreadedConnectionPool(
            minconn, maxconn,
            dbname=os.getenv("DB_NAME", "cloeila_dev"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=os.getenv("DB_PORT", "5432"),
            cursor_factory=RealDictCursor
        )
        if app:
            app.logger.info(f"[PostgreSQL] Initialized pool: {minconn}-{maxconn} connections")
    except Exception as e:
        if app:
            app.logger.error(f"[PostgreSQL] Pool initialization failed: {e}")
        else:
            print(f"[PostgreSQL] Pool initialization failed: {e}")

def get_postgres_connection():
    """
    Checks out a connection from the pool.
    Caller must call conn.close() to return it to the pool.
    Returns:
        psycopg2.connection or None if pool not initialized or error
    """
    global _pg_pool
    if _pg_pool is None:
        # Lazy-init with default sizes if not already done
        init_postgres_pool()
    try:
        return _pg_pool.getconn()
    except Exception as e:
        print(f"[PostgreSQL] Failed to get connection from pool: {e}")
        return None

def release_postgres_connection(conn):
    """
    Returns a connection to the pool. Call after done with conn.
    """
    global _pg_pool
    if _pg_pool and conn:
        _pg_pool.putconn(conn)
