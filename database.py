import sqlite3
from datetime import datetime

DB_NAME = "emotion_history.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_text TEXT NOT NULL,
            translated_text TEXT,
            emotion TEXT,
            created_at TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()

def save_analysis(original_text, translated_text, emotion):
    conn = get_connection()
    conn.execute(
        """
        INSERT INTO analyses
        (
            original_text,
            translated_text,
            emotion,
            created_at
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            original_text,
            translated_text,
            emotion,
            datetime.now()
        )
    )

    conn.commit()
    conn.close()

def get_recent_analyses(limit=20):
    conn = get_connection()
    rows = conn.execute(
        """
        SELECT *
        FROM analyses
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    ).fetchall()

    conn.close()
    return [dict (row) for row in rows]