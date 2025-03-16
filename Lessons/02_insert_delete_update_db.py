import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Studies"

)
#delete row that id = 318143062
# cursor = my_db.cursor()
# cursor.execute("DELETE FROM Students WHERE ID = 318143062;")
# cursor.execute("select * from Students;")
# res = cursor.fetchall()
# print("(ID(PRIMARY KEY)|NAME|AVERAGE)")
# print(res)

#insert rows
# cursor = my_db.cursor()
# sql = "INSERT INTO Students (ID, StudentName, Average) VALUES (%s, %s, %s)"
# values = [(413767819, 'Dvir', 95), (567189201, 'Shir', 100)]
# cursor.executemany(sql, values)
# cursor.execute("select * from Students;")
# res = cursor.fetchone()
# print("(ID(PRIMARY KEY)|NAME|AVERAGE)")
# while res is not None:
#     print(res)
#     res = cursor.fetchone()

#update rows
# cursor = my_db.cursor()
# sql = "INSERT INTO Students (ID, StudentName, Average) VALUES (%s, %s, %s)"
# values = [(413767819, 'Dvir', 95), (567189201, 'Shir', 100)]
# new_db = cursor.executemany(sql, values)
# cursor.execute("UPDATE Students SET Average = 100 WHERE Average > 90;")
# cursor.execute("select * from Students;")
# res = cursor.fetchone()
# print("(ID(PRIMARY KEY)|NAME|AVERAGE)")
# while res is not None:
#     print(res)
#     res = cursor.fetchone()

