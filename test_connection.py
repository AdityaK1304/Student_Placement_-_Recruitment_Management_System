
from database import connect_db

conn = connect_db()

if conn:
    print("MySQL Connected Successfully!")
    print("Python and MySQL Connected Successfully!")
    conn.close()
else:
    print("Connection Failed!")
