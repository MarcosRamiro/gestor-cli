import sqlite3
from pathlib import Path

DB_PATH = Path.home() / ".gestor_cli" / "data.db"


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS configs (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    conn.commit()


def set_config(key, value):
    conn = get_connection()
    conn.execute("INSERT OR REPLACE INTO configs VALUES (?, ?)", (key, value))
    conn.commit()


def get_config(key):
    conn = get_connection()
    cur = conn.execute("SELECT value FROM configs WHERE key=?", (key,))
    row = cur.fetchone()
    return row[0] if row else None
