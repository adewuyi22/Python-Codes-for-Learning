import mysql.connector

#To create a table in MySQL, use the "CREATE TABLE" statement.
#Make sure you define the name of the database when you create the connection

mydb = mysql.connector.connect(
  host="localhost",
  user="james",
  password="admin",
  database="mydatabase"
)

mycursor = mydb.cursor()

try:
    sql = ("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    mycursor.execute(sql)
    
    print("\nTable created successfully.")
except:
    print("\nTable already exist!")
  