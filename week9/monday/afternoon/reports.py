import mysql.connector
from db import get_connection
def get_summary() -> dict:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) AS total FROM soldiers")
    total = cursor.fetchone()["total"]
    cursor.execute("SELECT COUNT(*) AS active FROM soldiers WHERE active =TRUE")
    active = cursor.fetchone()["active"]
    cursor.close()
    conn.close()
    return {"total": total, "active": active, "inactive": total - active}

def count_by_unit() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                   SELECT `unit`,
                          COUNT(*) AS total
                   FROM soldiers
                   GROUP BY `unit`
                   ORDER BY total DESC;
                   """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_formatted_soldiers() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                   SELECT `id`,
                          `name`,
                            `rank`,
                          COALESCE(`rank`, 'unranked')   AS `rank`,
                          COALESCE(`unit`, 'unassigned') AS `unit`,
                          `active`
                   FROM soldiers;
                   """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    print(rows)
    return rows

def get_missing_data():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                   SELECT * FROM soldiers WHERE `rank` IS NULL 
                   """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_units_with_multiple_soldiers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                   SELECT `unit`,COUNT(*) AS total FROM soldiers GROUP BY `unit`
                       HAVING total > 1;
                   """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
