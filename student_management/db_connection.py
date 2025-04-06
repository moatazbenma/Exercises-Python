import mysql.connector

def connect_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="mtz",
            password='Mmoataz0000',
            database='db_student_management'
        )
        print("Database connected successfully ! ")
        return db
    except mysql.connector.Error as e:
        print("Error connecting to MySQL : ", e)
        return None
    
connect_db()