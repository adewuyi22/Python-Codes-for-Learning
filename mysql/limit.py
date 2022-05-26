import mysql.connector

#You can limit the number of records returned from the query, by using the "LIMIT" statement:

mydb = mysql.connector.connect(
  host="localhost",
  user="james",
  password="admin",
  database="mydatabase"
)
mycursor = mydb.cursor()

try:
  #This will print a record from 1 - 4
  #sql = "SELECT *FROM customers LIMIT 4" 

  #using the 'OFFSET' will allow you to print between a record from.
  #This will skip number 1 - 3 and print from 4 records from the table
  sql = "SELECT *FROM customers LIMIT 4 OFFSET 3" 


  mycursor.execute(sql)
  result=mycursor.fetchall()

  for x in result:
    print(x)
except:
  print("Error occured.")