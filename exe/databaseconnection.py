import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database = "newdb"
)
print(mydb, "connected")
#create new database
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE newdb")
#list of all your system database
#mycursor.execute("SHOW DATABASES")
#for i in mycursor:
#    print(i)




#create table :-customer
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")




#check if table exists or not.
'''mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)'''


#create new table with primary key
#mycursor.execute("CREATE TABLE customer1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")



#insert record into table :
'''
sql = "INSERT INTO customer1 (name,address) VALUES (%s,%s)"
val = [("jack","Rajkot"),
       ("tweensi","Pune"),
       ("raj","Rajkot"),
       ("Heni","Dubai"),
       ("meshvi","Rajkot"),
       ("rock","USA")]
mycursor.executemany(sql,val)

mydb.commit()
print(mycursor.rowcount, "record was inserted.")





#select records from table.

mycursor.execute("SELECT name,address FROM customer1")

fetchresult = mycursor.fetchone()
#for i in fetchresult:
print(fetchresult)'''




# select record by where statement :

sql = "SELECT * FROM customer1 WHERE address ='Rajkot'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
