import mysql.connector
import config



class Sale:
    def __init__(self, book_id, customer_id, quantity, total_price):
        self.book_id = book_id
        self.customer_id = customer_id
        self.quantity = quantity
        self.total_price = total_price


    def save(self):
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        ) 
        cursor = connection.cursor()

        sql = 'INSERT INTO sales (book_id, customer_id, quantity, total_price) VALUES (%s, %s, %s, %s)'
        values = (self.book_id, self.customer_id, self.quantity, self.total_price)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()

    def __str__(self):
        return f"Sale of Book ID {self.book_id} to Customer ID {self.customer_id} - Quantity: {self.quantity} - Total: $ {self.total_price}"

