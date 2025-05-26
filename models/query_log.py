"""
query_log.py
-------------
Tracks symbolic queries, transmutation calls, and system events.

Author: Khaylub Thompson-Calvin
Date: 2025-05-25

Purpose:
    - Store interaction logs per user (emotion, virtue, aura result, etc.)
    - Retrieve historical transmutation patterns
    - Export logs for reflection, analytics, or class advancement
    - Provide a universal `log_event()` shim used by other modules
"""

from datetime import datetime

# In-memory structure for now; swap to Mongo/Postgres later
query_logs = {}


def log_query(user_id, event_type, payload):
    """
    Stores a single symbolic query event.

    Parameters:
        user_id (str): The user's unique identifier
        event_type (str): e.g., 'transmutation', 'emotion_log', 'class_trigger'
        payload (dict): Context-specific data (emotion, virtue, aura, timestamp, etc.)
    """
    timestamp = datetime.utcnow().isoformat()

    if user_id not in query_logs:
        query_logs[user_id] = []

    query_logs[user_id].append({
        "event": event_type,
        "timestamp": timestamp,
        "details": payload
    })


def get_logs(user_id):
    """
    Retrieves all logs associated with a user.

    Parameters:
        user_id (str): The user's unique identifier

    Returns:
        list: List of log dictionaries
    """
    return query_logs.get(user_id, [])


def export_logs(user_id):
    """
    Returns logs in a structured, printable format.

    Parameters:
        user_id (str): The user's unique identifier

    Returns:
        list: List of human-readable strings summarizing the logs
    """
    logs = get_logs(user_id)
    return [
        f"{log['timestamp']} - [{log['event']}] → {log['details']}"
        for log in logs
    ]


def log_event(module: str, detail: str) -> dict:
    """
    Shim function used in other controllers to log general symbolic events.

    This is compatible with imports like:
        from models.query_log import log_event

    Parameters:
        module (str): Name of the system module (e.g., 'virtue', 'emotion', 'logic')
        detail (str): Human-readable or structured info (can be a dict or string)

    Returns:
        dict: The stored event object
    """
    timestamp = datetime.utcnow().isoformat()
    event = {
        "event": module,
        "timestamp": timestamp,
        "details": detail
    }

    if "system" not in query_logs:
        query_logs["system"] = []

    query_logs["system"].append(event)
    print(f"[LOG EVENT] {timestamp} :: [{module}] {detail}")
    return event
