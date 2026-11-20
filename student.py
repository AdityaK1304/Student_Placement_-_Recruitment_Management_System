
from database import connect_db


def get_students(keyword=""):
    conn = connect_db()
    if not conn:
        return []

    try:
        cursor = conn.cursor()
        search = f"%{keyword}%"

        cursor.execute("""
            SELECT * FROM students
            WHERE name LIKE %s
            OR email LIKE %s
            OR course LIKE %s
            ORDER BY student_id DESC
        """, (search, search, search))

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def add_student(name, email, course, percentage):
    conn = connect_db()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students
            (name, email, course, percentage)
            VALUES (%s, %s, %s, %s)
        """, (name, email, course, percentage))

        conn.commit()
        return True

    except Exception as e:
        print("Student Error:", e)
        return False

    finally:
        cursor.close()
        conn.close()


def update_student(student_id, name, email, course, percentage):
    conn = connect_db()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE students
            SET name=%s, email=%s, course=%s, percentage=%s
            WHERE student_id=%s
        """, (name, email, course, percentage, student_id))

        conn.commit()
        return cursor.rowcount > 0

    except Exception as e:
        print("Update Error:", e)
        return False

    finally:
        cursor.close()
        conn.close()


def delete_student(student_id):
    conn = connect_db()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM students WHERE student_id=%s",
            (student_id,)
        )
        conn.commit()
        return cursor.rowcount > 0

    except Exception as e:
        print("Delete Error:", e)
        return False

    finally:
        cursor.close()
        conn.close()
