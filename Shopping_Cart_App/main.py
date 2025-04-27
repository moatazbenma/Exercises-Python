from shopping_cart import Items
import csv

total = 0


def main():
    global total
    while True:
        print('\n1. Add Items')
        print("2. Remove Items")
        print("3. View Items")
        print("4. Update Items")
        print("5. Calculate Total")
        print("6. Export Purchases to CSV")
        print("7. Exit")

        try:
            choice = int(input('Enter your choice: '))
            if choice not in range(1, 8):
                print("❌ Invalid choice. Please enter a number between 1 and 7.")
                continue
        except ValueError as e:
            print(f"Error: {e}")
            continue

        if choice == 1:
            try:
                name = input("Enter name of product: ")
                price = float(input('Enter price of product: '))

                if price >= 50:
                    print("You GOT A 20% DISCOUNT!")
                    discount = price * 0.80
                    item = Items(name, price, discount)
                    item.add_items()
                    total += discount
                    print(f"The final price is: ${discount:.2f}")
                else:
                    print("No discount applied.")
                    no_discount = Items(name, price)
                    no_discount.add_items()

                    total += price
                    print(f"The final price is: ${price:.2f}")

            except ValueError as e:
                print(f"Error: {e}")
                continue

        elif choice == 2:
            try:
                id = int(input("Enter the ID of the item to remove:"))
                Items.remove_items(id)
            except ValueError as e:
                print(f"Error: {e}")
                continue

        elif choice == 3:
            print("Items in your cart: ")
            Items.view_items()



        elif choice == 4:
            try:
                id = int(input("Enter number of the product: "))
                name = input("Enter new name of the item: ")
                price = float(input("Enter new price of the item: "))

                if price >= 50:
                    print("You GOT A 20% DISCOUNT!")
                    discount = price * 0.80
                    updated_price = Items(name, price, discount)
                    updated_price.update_item(id)
                else:
                    print("No discount applied.")
                    no_updated_price= Items(name, price)
                    no_updated_price.update_item(id)

            except ValueError as e:
                print(f"Error: {e}")
                continue

        elif choice == 5:
            print(f"Your total price is: ${total:.2f}")

        elif choice == 6:
            Items.export_to_csv()



        elif choice == 7:
            print("Thanks for using the shopping cart. Goodbye! 🛒")
            break

        print("\n" + "-" * 40 + "\n")
        
main()
