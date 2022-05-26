import mysql.connector

''' Use the ORDER BY statement to sort the result in ascending or descending order.
    The ORDER BY keyword sorts the result ascending by default. 
    To sort the result in descending order, use the DESC keyword.
'''
mydb=mysql.connector.connect(
  host = "localhost",
  user = "james",
  password = "admin",
  database = "mydatabase"

)

mycursor=mydb.cursor()

#To sort the sort the result alphabeically by name:
try:
  sql = "SELECT *FROM customers ORDER BY name ASC" #You use "DESC" to sort in descending order
  mycursor.execute(sql)
  result=mycursor.fetchall()
  for x in result:
    print(x)
except:
  print("Error occured!")
