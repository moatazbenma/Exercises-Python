import mysql.connector

class Expense:
    def __init__(self, title, amount, category, date_now, description):
        self.title = title
        self.amount = amount
        self.category = category
        self.date_now = date_now
        self.description = description

    @staticmethod
    def get_connection():
        """Establish and return a database connection."""
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='mtz',
                password='Mmoataz0000',
                database='expense_tracker'
            )
            return connection
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")
            return None

    def save(self):
        """Save the expense to the database."""
        connection = self.get_connection()
        if connection is None:
            print("Unable to save expense due to a database connection error.")
            return

        try:
            cursor = connection.cursor()
            sql = 'INSERT INTO expenses (title, amount, category, date_now, description) VALUES (%s, %s, %s, %s, %s)'
            values = (self.title, self.amount, self.category, self.date_now, self.description)
            cursor.execute(sql, values)
            connection.commit()
            print(f"Expense '{self.title}' saved successfully!")
        except mysql.connector.Error as e:
            print(f"Error saving expense: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def view_all():
        """View all expenses from the database."""
        connection = Expense.get_connection()
        if connection is None:
            print("Unable to view expenses due to a database connection error.")
            return

        try:
            cursor = connection.cursor()
            sql = 'SELECT * FROM expenses'
            cursor.execute(sql)
            expenses = cursor.fetchall()
            print("\nAll Expenses\n")
            for expense in expenses:
                print(f"ID: {expense[0]} | Title: {expense[1]} | Amount: {expense[2]} | Category: {expense[3]} | Date: {expense[4]} | Description: {expense[5]}")
            print("\n")
        except mysql.connector.Error as e:
            print(f"Error retrieving expenses: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(expense_id):
        """Delete an expense by ID."""
        connection = Expense.get_connection()
        if connection is None:
            print("Unable to delete expense due to a database connection error.")
            return

        try:
            cursor = connection.cursor()
            sql = 'DELETE FROM expenses WHERE ID = %s'
            values = (expense_id,)
            cursor.execute(sql, values)
            connection.commit()
            if cursor.rowcount > 0:
                print(f"Expense with ID {expense_id} deleted successfully!")
            else:
                print(f"No expense found with ID {expense_id}.")
        except mysql.connector.Error as e:
            print(f"Error deleting expense: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(expense_id, title, amount, category, date_now, description):
        """Update an existing expense by ID."""
        connection = Expense.get_connection()
        if connection is None:
            print("Unable to update expense due to a database connection error.")
            return

        try:
            cursor = connection.cursor()
            sql = 'UPDATE expenses SET title = %s, amount = %s, category = %s, date_now = %s, description = %s WHERE ID = %s'
            values = (title, amount, category, date_now, description, expense_id)
            cursor.execute(sql, values)
            connection.commit()
            if cursor.rowcount > 0:
                print(f"Expense with ID {expense_id} updated successfully!")
            else:
                print(f"No expense found with ID {expense_id}.")
        except mysql.connector.Error as e:
            print(f"Error updating expense: {e}")
        finally:
            cursor.close()
            connection.close()

    def __str__(self):
        return f'Title: {self.title} | Amount: {self.amount} | Category: {self.category} | Date: {self.date_now} | Description: {self.description}'
