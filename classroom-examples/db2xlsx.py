import sqlite3
from mymodule import dump_table_to_xlsx
conn = sqlite3.connect("mydatabase.db")

dump_table_to_xlsx(conn,"books","books.xlsx")

conn.close()