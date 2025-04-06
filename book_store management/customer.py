import mysql.connector
import config


class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


    def save(self):
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        ) 
        cursor = connection.cursor()
        sql = 'INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)'
        values = (self.name, self.email, self.phone)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()

    def __str__(self):
        return f"{self.name} -  {self.email} - {self.phone}"
