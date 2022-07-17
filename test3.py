import mysql.connector as conn

mydb=conn.connect(host='localhost',user='root',password='Vijay@248621')
#print(mydb)
cursor=mydb.cursor() #creating cursor
#cursor.execute("create database sudhanshu")
#cursor.execute("show databases") #to execute query
#cursor.execute("create table sudhanshu.ineuron1(employee_id int(10),emp_name varchar(80),emp_mailid varchar(10),emp_salary int(6),emp_addendance int(3))")
#cursor.execute("alter table sudhanshu.ineuron1 modify emp_mailid varchar(80)")
cursor.execute("insert into sudhanshu.ineuron1 values(13,'sam','sam@ineuron.ai',104,34)")
mydb.commit()
cursor.execute("select * from sudhanshu.ineuron1")
#print(q2)
print(cursor.fetchall()) # it gives iterable object
# for i in cursor.fetchall():
#      print(i)
# # l=[]
# # for i in cursor.fetchall():
# #     l.append(i)
# # print(l)
