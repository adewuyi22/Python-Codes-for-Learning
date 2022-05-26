import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "james",
    password = "admin",
    database = "mydatabase"
)

#print(mydb)

db=mydb.cursor()
try:
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("Juliana", "45B Cool smile lane")
    db.execute(sql, val)

    mydb.commit()
    
    print (db.lastrowid, "\nRecord Inserted Successfully...")
    #print ("\nRecord Inserted Successfully...")
except:
    print("\nError Occured! check if Table exist.")


