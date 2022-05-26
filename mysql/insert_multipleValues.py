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
    val = [
        ("Adex", "22 Crescent street"),
        ("Tina", "45 Horse City"),
        ("James", "105 Creek Road"),
        ("Betty", "33 Freedom Street"),
        ("Collins", "54 Mba Street")
        
        ]
    db.executemany(sql, val)

    mydb.commit()
    
    print (db.lastrowid, "\nRecord Inserted Successfully...")
    #print ("\nRecord Inserted Successfully...")
except:
    print("\nError Occured! check if Table exist.")


