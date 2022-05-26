import mysql.connector

#creating a connection to the database.
#Use the username and password from your MySQL database:

mydb = mysql.connector.connect(
    host="localhost",
    user="james",
    password="admin"
)

#print(mydb)

#Deleting a database using the drop statement
mycursor=mydb.cursor()
try:
    mycursor.execute("DROP DATABASE mydatabase")
    print ("\nDatabase deleted successfully...")
except:
    print("\nDatabase does not exist for deleting!")

#To check if the database exist using the "SHOW DATABASE" statement.




