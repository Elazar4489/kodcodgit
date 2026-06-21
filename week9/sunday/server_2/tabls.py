import mysql.connector

soldiers = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db"
)

my_corsur = soldiers.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS soldiers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    ranki VARCHAR(50),
    unit VARCHAR(100), 
    active BOOLEAN DEFAULT TRUE
);
"""

# my_corsur.execute("DESCRIBE soldiers;")
# soldiers.commit()
# my_corsur.close()
# soldiers.close()

#====================================================================================


soldiers_rooms = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db"
)

my_corsur = soldiers_rooms.cursor()

create_table_query_2 = """
CREATE TABLE IF NOT EXISTS soldiers_rooms (
    id_door INT PRIMARY KEY AUTO_INCREMENT,
    members VARCHAR(100) NOT NULL,
    commander VARCHAR(50),
    in_the_base BOOLEAN DEFAULT TRUE
);
"""

my_corsur.execute(create_table_query_2)
my_corsur.execute("DESCRIBE soldiers_rooms;")
