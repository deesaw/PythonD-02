import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
SQL = """
SELECT * FROM books
"""
cursor.execute(SQL)

print(cursor.fetchone())
print("#"*50)
print(cursor.fetchmany(4))
print("#"*50)
print(cursor.fetchall())
print("#"*50)

cursor.execute(SQL)
for row in cursor:
	print(row)

cursor.execute(SQL)
for bookid,title,author in cursor:
	print(bookid,title,author)

conn.close()