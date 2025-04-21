from library_management_system import Library





def main():
    library = Library()
    while True:
        print("\n--------Library Management System----------")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Check Book")
        print("6. Display All Books")
        print("7. Exit")


        try:
            choice = int(input("Enter your choice : "))
        except ValueError as e:
            print(f"Error : {e}")


        if choice == 1:
            title = input("Enter book title : ")
            author = input("Enter author name : ")
            library.add_book(title, author)

        elif choice == 2:
            title = input("Enter book title : ")
            library.remove_book(title)

        elif choice == 3:
            title = input("Enter book title : ")
            library.borrow_book(title)
        
        elif choice == 4:
            title = input("Enter book title : ")
            library.return_book(title)

        elif choice == 5:
            title = input("Enter book title : ")
            library.check_availability(title)

        elif choice == 6:
            library.view_book()

        elif choice == 7:
            print("Exiting ....")
            break

        else: 
            print('Error ! try again')




main()