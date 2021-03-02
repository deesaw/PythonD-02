import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
SQL = """
INSERT INTO books (title, author)
VALUES("Wings of Fire","Abdul Kalam")
"""
cursor.execute(SQL)
print("{} rows inserted".format(cursor.rowcount))
conn.commit()
conn.close()