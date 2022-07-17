import mysql.connector as conn

mydb=conn.connect(host='localhost',user='root',password='Vijay@248621')
#print(mydb)
cursor=mydb.cursor()
#cursor.execute("create database vijay")
#cursor.execute("show databases")
cursor.execute("create Table vijay.ineuron(employee_id int(10),emp_name varchar(80),emp_mailid varchar,emp_salary int(6),emp_attendance int(3))")
#print(cursor.fetchall())

