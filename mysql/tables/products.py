import mysql.connector

mydb = mysql.connector.connect (
host = "localhost",
user = "james",
password = "admin",
database = "mydatabase"
)

db=mydb.cursor()

try:
  sql = "CREATE TABLE products (id  INT AUTO_INCREMENT PRIMARY KEY, pname VARCHAR(255))"
  db.execute(sql)
  print("\n Products Table created successfully...")
  
except:
  print("\n Products Table already exist!")

