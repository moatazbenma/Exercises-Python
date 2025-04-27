import mysql.connector
import config



def connection_db():
    try:
        db = mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
        )

        return db
    except Exception as e:
        print(f"Error : {e}")

