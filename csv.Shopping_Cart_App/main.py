from shopping_cart import Cart


def main():

    while True:
        print("-----Shopping Cart------")
        print("\n1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. View Items")
        print('5. Export it to csv')
        print("6. Exit")


        try:
            choice = int(input("Choose an option : "))
            print('\n')
        except ValueError as e:
            print(f"Error {e}")
            continue 


        if choice == 1:
            try:
                id = int(input("Enter the id of the product : "))
                name = input("Enter the name of the product : ")
                price = int(input("Enter the price of the product : "))
            except ValueError as e:
                print(f"Error : {e}")
                continue


            if price >= 50:
                discount = price * 0.80
                item_discount = Cart(id, name, price, discount)
                item_discount.add_item()
            else:
                item_no_discount = Cart(id, name, price)
                item_no_discount.add_item()

        elif choice == 2:
            try:
                id = int(input("Enter the id of the product : "))
                name = input("Enter the name of the product : ")
                price = int(input("Enter the price of the product : "))
            except ValueError as e:
                print(f"Error : {e}")
                continue

            if price >= 50:
                discount = price * 0.80
                item_discount = Cart(id, name, price, discount)
                item_discount.update_item()
            else:

                item_no_discount = Cart(id, name, price)
                item_no_discount.update_item()


        elif choice == 3:
            try:
                id = int(input("Enter the id of the product : "))
            except ValueError as e:
                print(f"Error : {e}")
                continue

            remove = Cart(id)
            remove.remove_item()


        elif choice == 4:
            view_item = Cart()
            view_item.view_items()


        elif choice == 5:
            export = Cart()
            export.export_csv()
            
            print("✅ File exported successfully ")

        elif choice == 6:
            print("Exiting....")
            break

        else:
            print("Error !")
            return


        print("\n" + 40 * '-' + '\n')
main()