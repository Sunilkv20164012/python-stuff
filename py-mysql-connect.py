print("hello-world")

import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="sunil",passwd="1234",database="sunillinus")

mycursor = mydb.cursor()

#mycursor.execute("show databases")
#mycursor.execute("create database sunillinus")
#mycursor.execute("use sunillinus")
#mycursor.execute("create table students(name varchar(20),college varchar(20))")
#mycursor.execute("insert into students values ('navin','vsit'),('priya','bvit')")
mycursor.execute("select * from students")

result = mycursor.fetchone()

for i in result:
	print(i)
