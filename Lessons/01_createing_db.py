import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Studies"

)
cursor = my_db.cursor()
cursor.execute("select * from Students;")
res = cursor.fetchone()
print("(ID(PRIMARY KEY)|NAME|AVERAGE)")
while res is not None:
    print(res)
    res = cursor.fetchone()