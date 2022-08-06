import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", passwd = "Kshevale0077@0077",use_pure=True)

query = "show databases"

cursor = mydb.cursor()
# cursor.execute("create database abcdef")
# cursor.execute("Create table abcdef.ineuron(emp_id int, emp_name varchar(80), emp_mailid varchar(20), emp_salary int, emp_attendance int)")

s = "insert into abcdef.ineuron values(101,'Gaurav Ratan','gaurav@gmail.com',1000,30)"#5 Columns so we need to give 5 values for that
s = "insert into abcdef.ineuron values(102,'Gaurav Ratan','gaurav@gmail.com',1000,10)"
cursor.execute(s)
mydb.commit()
# print(cursor.fetchall())
# cursor.execute("select * from abcdef.ineuron")
cursor.execute("select emp_name, emp_id from abcdef.ineuron where emp_attendance = 10 ")
# cursor.execute("select * from abcdef.ineuron")
for i in cursor.fetchall():
    print(i)




