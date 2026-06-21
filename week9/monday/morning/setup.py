import mysql.connector

def create_database():
    cnx = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
    )
    my_cursor = cnx.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTs db;")
    my_cursor.close()
    cnx.close()



def create_table_schema():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "db"
    )
    my_cursor = cnx.cursor()
    query = """CREATE TABLE IF NOT EXISTS soldiers (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), ranki VARCHAR(50), unit VARCHAR(100), active BOOLEAN DEFAULT TRUE);"""

    my_cursor.execute(query)
    print("jj")
    my_cursor.close()
    cnx.close()

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







if __name__ == '__main__':
    create("Elazar Altman", "student", "unit 8200")