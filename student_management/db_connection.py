import mysql.connector
import config

def connect_db():
    try:
        db = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        print("Database connected successfully ! ")
        return db
    except mysql.connector.Error as e:
        print("Error connecting to MySQL : ", e)
        return None
    
connect_db()