import mysql.connector
def get_connection():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db"
    )
    return cnx

def create(name: str, rank: str, unit: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO soldiers (name, ranki, unit) VALUES (%s, %s, %s)"
    values = (name, rank, unit)
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid # MySQL gives us the id it assigned
    cursor.close()
    conn.close()
    return new_id

def update(soldier_id: int, data: dict) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    # Build the SET clause dynamically from the dict
    set_parts = [f"{key} = %s" for key in data.keys()]
    set_clause = ", ".join(set_parts)
    sql = f"UPDATE soldiers SET {set_clause} WHERE id = %s"
    values = list(data.values()) + [soldier_id]
    cursor.execute(sql, values)
    conn.commit()
    changed = cursor.rowcount > 0 # False if id did not exist
    cursor.close()
    conn.close()
    return changed

def delete(soldier_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM soldiers WHERE id = %s", (soldier_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return deleted

def get_all() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) # returns dicts instead of tuples
    cursor.execute("SELECT * FROM soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_by_id(soldier_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE id = %s", (soldier_id,))
    row = cursor.fetchone() # returns one dict or None
    cursor.close()
    conn.close()
    return row

if __name__ == "__main__":
    print(get_by_id(4))

