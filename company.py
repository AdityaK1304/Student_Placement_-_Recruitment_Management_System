
from database import connect_db


def get_companies():
    conn = connect_db()
    if not conn:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM companies ORDER BY company_id DESC")
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def add_company(name, role, package):
    conn = connect_db()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO companies
            (company_name, job_role, package)
            VALUES (%s, %s, %s)
        """, (name, role, package))

        conn.commit()
        return True

    except Exception as e:
        print("Company Error:", e)
        return False

    finally:
        cursor.close()
        conn.close()
