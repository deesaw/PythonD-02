import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
SQL = """
CREATE TABLE IF NOT EXISTS ips(
rowid integer primary key,
ip text
)
"""
cursor.execute(SQL)
print("Table created")

from mymodule import get_ips_from_xlsx
myips = [(ip,) for ip in get_ips_from_xlsx("ips.xlsx")]
#print(myips)

SQL = """
INSERT INTO ips(ip)
VALUES(?)
"""
cursor.executemany(SQL,myips)
print("{} rows inserted".format(cursor.rowcount))
conn.commit()
conn.close()