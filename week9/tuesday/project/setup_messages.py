import mysql.connector

cnx = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "root",
    database = "db"
)

cursor = cnx.cursor(dictionary=True)

# query = cursor.execute("""
#     CREATE TABLE IF NOT EXISTS intel_messages (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     unit VARCHAR(100) NOT NULL,
#     classification ENUM('unclassified','confidential','secret','top_secret'),
#     content TEXT NOT NULL,
#     source VARCHAR(100),
#     created_at DATETIME DEFAULT NOW());
# """)
# p = cursor.execute("DESCRIBE intel_messages;")
# print(p)

# cursor.execute("SHOW COLUMNS FROM intel_messages;")
# columns = cursor.fetchall()
# list_of_columns = [{"column": col[0], "type": col[1]} for col in columns]
#
#
# for i in list_of_columns:
#     print(i)


cursor.execute("INSERT INTO intel_messages (unit, classification, content) VALUES ('aaa', 'unclassified', 'ccc');")
rows = cursor.fetchall()
print(rows)