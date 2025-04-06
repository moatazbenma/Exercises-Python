import datetime

expenses = {}
expense_id = 1


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        try:
            user = int(input("Choose an option: "))
            if user == 1:
                add_expense()
            elif user == 2:
                view_expense()
            elif user == 3:
                total_expense()
            elif user == 4:
                print("Have a good day!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def add_expense():
    global expense_id
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    expenses[expense_id] = {
        'date': date,
        'amount': amount,
        'category': category,
        'description': description
    }
    expense_id += 1

    print("Expense added successfully!")


def view_expense():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nDate       | Amount  | Category  | Description")
    print("------------------------------------------------")

    for expense in expenses.values():
        print(f"{expense['date']} | {expense['amount']:.2f}  | {expense['category']} | {expense['description']}")


def total_expense():
    total = sum(expense['amount'] for expense in expenses.values())
    print(f"Total expenses: {total:.2f}")


if __name__ == "__main__":
    main()
