import mysql.connector

conn = mysql.connector.connect(user ='root', password='',host='localhost',database='pytest')

mycursor = conn.cursor()
mycursor.execute("delete from employee where id=2;")
conn.commit()
