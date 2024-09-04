import sqlite3

conn = sqlite3.connect("pokemon2.db")

c = conn.cursor()

c.execute(
    """
CREATE TABLE type (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL
)
"""
)
conn.commit()
conn.close()
