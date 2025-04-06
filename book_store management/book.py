import mysql.connector
import config


class Book:
    def __init__(self, title, author, genre, price, stock):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock = stock

    def save(self):
        connection = mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
        ) 
        cursor = connection.cursor()
        sql = "INSERT INTO books (title, author, genre, price, stock) VALUES (%s, %s, %s, %s, %s)"
        values = (self.title, self.author, self.genre, self.price, self.stock)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()

    def __str__(self):
        return f"{self.title} by {self.author} -  {self.genre} - ${self.price} - Stock : {self.stock}"