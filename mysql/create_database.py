import mysql.connector

#creating a connection to the database.
#Use the username and password from your MySQL database:

mydb = mysql.connector.connect(
    host="localhost",
    user="james",
    password="admin"
)

#print(mydb)

#creating a database "mydatabase"
mycursor=mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE mydatabase")
    print ("\nDatabase created successfully...")
except:
    print("\nDatabase already exist!")



