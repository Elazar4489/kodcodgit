import mysql.connector
def create_table_schema() -> str:
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "db"
    )
    my_cursor = cnx.cursor()
    query = """
            CREATE TABLE IF NOT EXISTS soldiers (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100), 
                rank VARCHAR(50), 
                unit VARCHAR(100), 
                active BOOLEAN DEFAULT TRUE
                );
            """

    my_cursor.execute(query)
    my_cursor.close()
    cnx.close()
    return "Table Created!"
