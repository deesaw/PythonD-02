import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
SQL = """
SELECT * FROM books
"""
cursor.execute(SQL)
print(cursor.fetchall())
conn.close()