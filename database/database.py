import mysql.connector

conn = mysql.connector.connect(user ='root', password='',host='localhost',database='pytest')

mycursor = conn.cursor()
#mycursor.execute("SHOW TABLES")
#print(mycursor.fetchall())


# Creating tables

#mycursor.execute("create table student(id int primary key, name varchar(30), dob datetime, email varchar(20));")
#print(mycursor.fetchall())

mycursor.execute("SHOW TABLES")
print(mycursor.fetchall())