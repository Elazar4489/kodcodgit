import datetime

import mysql.connector


def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "root",
        database = "db"
    )
    return conn
    """
    mycursor = conn.cursor()
    query = ("SELECT id, name, ranki, unit, active FROM soldiers "
             "WHERE hire_date BETWEEN %s and %s")

    hire_start = datetime.date(2020, 3,4)
    hire_end = datetime.date(2020, 3, 9)
    mycursor.execute(query, (hire_start, hire_end))

    for (id, name, ranki, unit, active) in mycursor:
    """

def get_schema_of_soldiers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DESCRIBE soldiers;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"column": row[0], "type": row[1]} for row in rows]

def get_schema_of_soldiers_rooms():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DESCRIBE soldiers_rooms;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"column": row[0], "type": row[1]} for row in rows]


# def add_soldier(name, ranki, unit, active = True):
