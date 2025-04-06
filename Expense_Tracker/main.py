from add_expense import Expense


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        choice = int(input("Choose an option : "))

        if choice == 1:
            title = input("Title : ")
            amount = float(input("Amount : "))
            category = input("Category : ")
            date_now = input("Date (YYYY-MM-DD): ")
            description = input("Description : ")
            expense = Expense(title, amount, category, date_now, description)
            expense.save()


        elif choice == 2:
            Expense.view_all()

        elif choice == 3:
            ID = int(input("Enter Expense ID to update : "))
            title = input("New Title : ")
            amount = float(input("New Amount : "))
            category = input("New Category : ")
            date_now = input("New Date (YYYY-MM-DD): ")
            description = input("New Description: ")
            Expense.update(ID, title, amount, category, date_now, description)

        elif choice == 4:
            ID = int(input("Enter Expense ID to delete : "))
            Expense.delete(ID)

        elif choice == 5:
            print("Exiting.....")
            break
    
        else:
            print("Invalid choice try again.")



if __name__ == "__main__":
    main()