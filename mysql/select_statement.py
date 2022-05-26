import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="james",
  password="admin",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM products"

try:
  
  mycursor.execute(sql)
  
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

except:
  print("Error occured.")
  