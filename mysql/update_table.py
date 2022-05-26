import mysql.connector

mydb=mysql.connector.connect(
    host = "localhost",
    user = "james",
    password = "admin",
    database = "mydatabase"
)
mycursor=mydb.cursor()
sql = "UPDATE customers SET address = %s WHERE ID = %s"
val = ("121 Iponri Street", "3")

try:

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) afected")    

except:
    print("\nError Occured!")
