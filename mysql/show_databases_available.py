import mysql.connector

mydb=mysql.connector.connect(
    host = "localhost",
    user = "james",
    password = "admin",
    database = "mydatabase"
)
mycursor=mydb.cursor()

try:
    print("\nBelow are the list of Databases available:\n")
    sql = "SHOW tables"
    
    mycursor.execute(sql)
    for x in mycursor:
        print(x)
    
except:
    print("No Database found.")
