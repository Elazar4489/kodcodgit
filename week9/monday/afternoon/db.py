import mysql.connector
def get_connection():
    cnx = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "db"
    )
    return cnx

def show_all():
    cnx = get_connection()
    my_cursor = cnx.cursor()
    my_cursor.execute("SELECT * FROM soldiers;")
    rows = my_cursor.fetchall()
    cnx.commit()
    my_cursor.close()
    cnx.close()
    return rows

def show_one(ind: int):
    cnx = get_connection()
    my_cursor = cnx.cursor()
    my_cursor.execute("SELECT * FROM soldiers WHERE id = (%s);", (ind,))
    row = my_cursor.fetchone()
    cnx.commit()
    my_cursor.close()
    cnx.close()
    return row

def create(name, rank, unit):
    cnx = get_connection()
    my_cursor = cnx.cursor()
    sql = "INSERT INTO soldiers (`name`, `rank`, `unit`) VALUES (%s, %s, %s)"
    values = (name, rank, unit)
    my_cursor.execute(sql, values)
    new_id = my_cursor.lastrowid
    cnx.commit()
    my_cursor.close()
    cnx.close()
    return new_id

def update(ind: int, data: dict):
    cnx = get_connection()
    my_cursor = cnx.cursor()
    set_parts = [f"`{key}` = %s" for key in data.keys()]
    set_clause = ", ".join(set_parts)
    sql = f"UPDATE soldiers SET {set_clause} WHERE id = %s"
    values = list(data.values()) + [ind]
    my_cursor.execute(sql, values)
    changed = my_cursor.rowcount > 0
    cnx.commit()
    my_cursor.close()
    cnx.close()
    return changed

def delete(ind):
    cnx = get_connection()
    my_cursor = cnx.cursor()
    my_cursor.execute("DELETE FROM soldiers WHERE id = %s", (ind,))
    changed = my_cursor.rowcount > 0
    cnx.commit()
    my_cursor.close()
    cnx.close()
    return  changed