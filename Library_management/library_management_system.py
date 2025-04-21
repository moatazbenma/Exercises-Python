import json






class Library:
    def __init__(self, file_name='library.json'):
        self.file_name = file_name
        self.books = self.load_book()

    def load_book(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    def save_book(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = {'author': author, 'available': True}
            self.save_book()
            print(f"✅ {title} has been added to the library!")
        else:
            print("❌ Error : The book is already added, you can't add it again !")


    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            self.save_book()
            print(f"{title} has removed from the library")
        else: 
            print("❌Error : That book was not found !")

    def borrow_book(self, title):
        if title in self.books:
            if self.books[title]['available']: 
                self.books[title]['available'] = False
                self.save_book()
                print(f"✅ You borrowed '{title}'.")
            else:
                print(f"❌ '{title}' is already borrowed.")

        else:
            print(f"❌ '{title}' not found in the library.")
            
    def return_book(self, title):
        if title in self.books:
            if not self.books[title]['available']:
                self.books[title]['available'] = True
                self.save_book()
                print(f"{title} has returned to the library !")
            else:
                print(f"❌ '{title}' was not borrowed, so it can't be returned.")

        else:
            print(f"❌ Error : {title} not found in the library ! ")


    def check_availability(self, title):
        if title in self.books:
            status = "available" if self.books[title]['available'] else "not available"
            print(f"✅ '{title}' is {status}.")
        else:
            print(f"❌ '{title}' doesn't exist in the library.")

    def view_book(self):
        if not self.books:
            print("No books in the library")
        
        else:
            for title, details in self.books.items():
                status = 'available' if details['available'] else 'not available'
                print(f"{title}----by {details['author']}-----This book is : {status}")






 