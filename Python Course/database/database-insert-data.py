import mysql.connector

conn = mysql.connector.connect(user ='root', password='',host='localhost',database='pytest')

mycursor = conn.cursor()
#mycursor.execute("insert into employee(id,name,dob,email) values(2,'ronald','1989-09-20','python@py3.py');")
#conn.commit()


#Retrieveng data
mycursor.execute("SELECT * FROM employee")
print(mycursor.fetchall())