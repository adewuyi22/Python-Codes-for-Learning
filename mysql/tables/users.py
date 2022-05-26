import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="james",
  password="admin",
  database="mydatabase"
)
db = mydb.cursor()

try:
     
    db.execute("CREATE TABLE users (ID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(50)) ")
    print("\nusers table created successfully.")
except:
    print("\n users Table already created!")
