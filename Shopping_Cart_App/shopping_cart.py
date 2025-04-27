from connection import connection_db
import csv


class Items:
    def __init__(self, name, price, discounted_price=None):
        self.name = name
        self.price = price
        self.discounted_price = discounted_price

    def add_items(self):
        try:
            if self.price < 0:
                raise ValueError("Price cannot be negative.")
            
            db = connection_db()
            with db.cursor() as cursor:
                sql = 'INSERT INTO items(name, price, discounted_price) VALUES(%s, %s, %s)'
                values = (self.name, self.price, self.discounted_price)
                cursor.execute(sql, values)
                db.commit()
            
            print("✅ Item added successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if db:
                db.close()

    @staticmethod
    def view_items():
        try:
            db = connection_db()
            with db.cursor() as cursor:
                sql = 'SELECT id, name, price, discounted_price FROM items'
                cursor.execute(sql)
                items = cursor.fetchall()

                if not items:
                    print("⚠️ No items found.")
                else:
                    for item_id, name, price, discounted_price in items:
                        print(f"ID: {item_id} / Name: {name} / Regular_Price: ${price}/ Discounted_Price: ${discounted_price}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if db:
                db.close()

    def update_item(self, id):
        try:
            if self.price < 0:
                raise ValueError("Price cannot be negative.")
            
            db = connection_db()
            with db.cursor() as cursor:
                sql = 'UPDATE items SET name = %s, price = %s, discounted_price = %s WHERE id = %s'
                values = (self.name, self.price, self.discounted_price, id)
                cursor.execute(sql, values)
                db.commit()

                if cursor.rowcount == 0:
                    print("⚠️ No item found with that ID.")
                else:
                    print("✅ Item updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if db:
                db.close()

    @staticmethod
    def remove_items(id):
        try:
            db = connection_db()
            with db.cursor() as cursor:
                sql = 'DELETE FROM items WHERE id = %s'
                values = (id,)
                cursor.execute(sql, values)
                db.commit()

                if cursor.rowcount == 0:
                    print("⚠️ No item found with that ID.")
                else:
                    print("✅ Item removed successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if db:
                db.close()

    @staticmethod
    def export_to_csv():
        try:
            db = connection_db()
            with db.cursor() as cursor:
                sql = 'SELECT name, price, discounted_price FROM items'
                cursor.execute(sql)
                items = cursor.fetchall()

                with open('purchases.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Item Name', 'Price', 'Discounted_Price'])
                    for name, price, discounted_price in items:
                        writer.writerow([name, price, discounted_price])

                print("✅ Purchases exported to purchases.csv successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if db:
                db.close()



    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
