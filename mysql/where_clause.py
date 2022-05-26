import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="james",
  password="admin",
  database="mydatabase"
)

mycursor = mydb.cursor()

try:
    #using WHERE clause
    mycursor.execute("SELECT * FROM customers WHERE ID = '2'")
  
  #using LIKE clause
  #  mycursor.execute("SELECT * FROM customers WHERE name LIKE '%mes'")
  
    myresult = mycursor.fetchall()
    print("\n",myresult)

#  for x in myresult:
#   print(x)

except:
  print("Error occured.")