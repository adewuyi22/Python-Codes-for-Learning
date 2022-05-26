import mysql.connector

#You can delete records from an existing table by using the "DELETE FROM" statement:
mydb = mysql.connector.connect(
  host="localhost",
  user="james",
  password="admin",
  database="mydatabase"
)
mycursor = mydb.cursor()

try:
    #The "%s" is use to escape values in the delete statement:
    #This is to prevent SQL injections, 
  sql = "DELETE FROM customers WHERE name = '%s'" 
  name = "tina"

  result  = mycursor.execute(sql, name)
  mydb.commit()
  print(mycursor.rowcount, "records(s) deleted")
  
except:
  print("Error occured.")
  