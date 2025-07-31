import mysql.connector   

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="atul123",
    database="face_recognizer",
   
   
   
)
my_cursor=conn.cursor()

conn.commit()
conn.close()
print("connection")