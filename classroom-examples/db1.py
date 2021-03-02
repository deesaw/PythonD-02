import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
SQL = """
CREATE TABLE IF NOT EXISTS books(
bid integer primary key,
title text,
author text
)
"""
cursor.execute(SQL)
print("Table created")
conn.close()