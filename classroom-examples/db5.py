import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
SQL = """
INSERT INTO books (title, author)
VALUES(?,?)
"""

mybooks =[
("5 AM Club","Robin Sharma"),
("My Experiments with Truth","MK Gandhi"),
("My Experiments with Food","Ramesh S")
]

cursor.executemany(SQL,mybooks)
print("{} rows inserted".format(cursor.rowcount))
conn.commit()
conn.close()