from book import Book
from customer import Customer
from sales import Sale

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    book = Book(title, author, genre, price, stock)
    book.save()
    print("Book added successfully!")

def add_customer():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    customer = Customer(name, email, phone)
    customer.save()
    print("Customer added successfully!")

def record_sale():
    book_id = int(input("Book ID: "))
    customer_id = int(input("Customer ID: "))
    quantity = int(input("Quantity: "))
    total_price = float(input("Total Price: "))
    sale = Sale(book_id, customer_id, quantity, total_price)
    sale.save()
    print("Sale recorded successfully!")

def main():
    print("\n=== Bookstore Management System ===")
    print("1. Add Book")
    print("2. Add Customer")
    print("3. Record Sale")
    print("4. Exit")
    choice = input("Choose an option: ").strip()

    if choice == '1':
        add_book()
    elif choice == '2':
        add_customer()
    elif choice == '3':
        record_sale()
    elif choice == '4':
        print("Exiting... Goodbye!")
        exit()
    else:
        print("Invalid Choice!")

if __name__ == "__main__":
    while True:
        main()
