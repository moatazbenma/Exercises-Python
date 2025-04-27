import json
import csv

class Cart:

    def __init__(self, id=None, name=None, price=None, discounted_price=None):
        self.id = id
        self.name = name
        self.price = price
        self.discounted_price = discounted_price
        self.cart = self.load_item()

    def load_item(self):
        try:
            with open('cart.json', mode='r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"ERROR : {e}")
            return {}
            
    def save_item(self):
        with open('cart.json', mode='w') as file:
            json.dump(self.cart, file, indent=4)


    

    def add_item(self):
        if str(self.id) not in self.cart:
            self.cart[str(self.id)] = {'Name': self.name, 'Price': self.price, 'Discounted_price': self.discounted_price}
            self.save_item()

            if self.price >= 50:
                print("you got 20% discount 😊")
            else:
                print("you didn't get discount 😔")

            print("✅ Item added to cart. ")
        else:
            print("This product already there ! ")
            

    def update_item(self):
        if str(self.id) in self.cart:
            self.cart[str(self.id)] = {'Name': self.name, 'Price':self.price, 'Discounted_price':self.discounted_price}
            self.save_item()

            if self.price >= 50:
                print("you got 20% discount 😊")
            else:
                print("you didn't get discount 😔")

            print("✅ Item Updated.")
            
        else:
            print("❌ product not found !")

    def remove_item(self):
        if str(self.id) in self.cart:
            del self.cart[str(self.id)]
            self.save_item()
            print("✅ Item Removed")
        else:
            print("❌ Product not found!")


    def view_items(self):
        if self.cart:
            for id, item in self.cart.items():
                print(f"ID : {str(id)} /Name of the product :  {item['Name']} /Regular Price : {item['Price']} /Discounted Price: {item['Discounted_price']}\n{'-'*30}")
        else:
            print("Empty !")


    def export_csv(self):
        with open("cart.csv", mode='w', newline='') as file:
            write = csv.writer(file)
            write.writerow(['Id', 'Name', 'Price', 'Discounted Price'])

            for id in sorted(self.cart, key=lambda x: int(x)):
                item = self.cart[id]
                write.writerow([id, item['Name'], item['Price'], item['Discounted_price']])