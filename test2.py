import mysql.connector as conn
mydb=conn.connect(host='localhost',user='root',password='Vijay@248621')
cursor=mydb.cursor()
cursor.execute("insert into sudhanshu.ineuron1 values(101,'sudhanshu','sudhanshu@ineuron.ai',100,30)")
cursor.execute("select * from sudhanshu.ineuron1")
mydb.commit()
#unless you commit the inserted data will notreflect
cursor.execute("select emp_id,emp_mailid from sudhanshu.ineuron1")
for i in cursor.fetchall():
    print(i)
l=[]
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l[0]))
