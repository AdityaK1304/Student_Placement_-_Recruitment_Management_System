
import os
import mysql.connector


def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("MYSQL_PASSWORD", ""),
            database="placement_db"
        )
        return conn

    except mysql.connector.Error as e:
        print("Database Connection Error:", e)
        return None
