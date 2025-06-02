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
from typing import Union

# In-memory structure for now; to be upgraded to Mongo/Postgres later
query_logs = {}


def log_query(user_id: str, event_type: str, payload: dict) -> dict:
    """
    Stores a single symbolic query event.

    Args:
        user_id (str): The user's unique identifier
        event_type (str): e.g., 'transmutation', 'emotion_log', 'class_trigger'
        payload (dict): Context-specific data (emotion, virtue, aura, etc.)

    Returns:
        dict: The saved event structure
    """
    timestamp = datetime.utcnow().isoformat()
    event = {
        "event": event_type,
        "timestamp": timestamp,
        "details": payload
    }

    if user_id not in query_logs:
        query_logs[user_id] = []

    query_logs[user_id].append(event)
    return event


def get_logs(user_id: str) -> list:
    """
    Retrieves all logs associated with a user.

    Args:
        user_id (str): The user's unique identifier

    Returns:
        list: List of log dictionaries
    """
    return query_logs.get(user_id, [])


def export_logs(user_id: str) -> list:
    """
    Returns logs in a structured, printable format.

    Args:
        user_id (str): The user's unique identifier

    Returns:
        list: List of human-readable strings summarizing the logs
    """
    logs = get_logs(user_id)
    return [
        f"{log['timestamp']} - [{log['event']}] → {log['details']}"
        for log in logs
    ]


def log_event(module: str, detail: Union[str, dict]) -> dict:
    """
    Logs a general symbolic system event (not tied to user).

    Args:
        module (str): Name of the system module (e.g., 'virtue', 'emotion', 'lapis_index')
        detail (str | dict): Human-readable or structured info

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
