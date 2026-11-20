
from database import connect_db


def get_placements():
    conn = connect_db()
    if not conn:
        return []

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                p.placement_id,
                s.name,
                c.company_name,
                c.job_role,
                c.package,
                p.status
            FROM placements p
            JOIN students s
                ON p.student_id = s.student_id
            JOIN companies c
                ON p.company_id = c.company_id
            ORDER BY p.placement_id DESC
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def add_placement(student_id, company_id, status):
    conn = connect_db()
    if not conn:
        return False

    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO placements
            (student_id, company_id, status)
            VALUES (%s, %s, %s)
        """, (student_id, company_id, status))

        conn.commit()
        return True

    except Exception as e:
        print("Placement Error:", e)
        return False

    finally:
        cursor.close()
        conn.close()
