import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="james",
  password="admin",
  database="mydatabase"
)
db = mydb.cursor()

try:
    #sql = "DROP TABLE IF EXISTS customers" 
    db.execute("DROP TABLE products")
    print("\nTable deleted successfully.")
except:
    print("\nTable does not exist for deleting!")