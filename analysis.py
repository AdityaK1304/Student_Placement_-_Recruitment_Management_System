
from database import connect_db


def get_placement_analysis():
    conn = connect_db()

    if not conn:
        return {
            "total": 0,
            "selected": 0,
            "rejected": 0,
            "pending": 0,
            "average_package": 0
        }

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*) FROM placements
        """)
        total = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM placements
            WHERE LOWER(status) = 'selected'
        """)
        selected = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM placements
            WHERE LOWER(status) = 'rejected'
        """)
        rejected = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM placements
            WHERE LOWER(status) = 'pending'
        """)
        pending = cursor.fetchone()[0]

        cursor.execute("""
            SELECT AVG(c.package)
            FROM placements p
            JOIN companies c ON p.company_id = c.company_id
            WHERE LOWER(p.status) = 'selected'
        """)
        average = cursor.fetchone()[0] or 0

        return {
            "total": total,
            "selected": selected,
            "rejected": rejected,
            "pending": pending,
            "average_package": round(float(average), 2)
        }

    finally:
        cursor.close()
        conn.close()
