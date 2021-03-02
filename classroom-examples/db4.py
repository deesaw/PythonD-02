import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
SQL = """
INSERT INTO books (title, author)
VALUES("Wings of Fire","Abdul Kalam")
"""
try:
	cursor.execute(SQL)
except Exception as err:
	print(type(err),err)
	print("Something went wrong, rolling back")
	conn.rollback()
else:
	print("All is well, commiting")
	print("{} rows inserted".format(cursor.rowcount))
	conn.commit()
finally:
	print("Entering finally clause,closing connection")
	conn.close()