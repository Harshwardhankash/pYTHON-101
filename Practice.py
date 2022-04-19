import mysql.connector

mydb = mysql.connector.connect(

  host="localhost",
  user="root",
  password="MOBIGESTURe"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

import mysql.connector

mydb = mysql.connector.connect(


  host="localhost", 
  user="root",
  password="MOBIGESTURe",
  database="mydatabase"

)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers1 (name VARCHAR(255), address VARCHAR(255))")
mport mysql.connector

mydb = mysql.connector.connect(

  host="localhost",
  user="root",
  password="MOBIGESTURe",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MOBIGESTURe",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MOBIGESTURe",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")