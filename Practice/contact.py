def main_m():
    contacts = {}
    while True:
        print("------Contact-------\n\n")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Update Contact")
        print("4. Remove Contact")
        print("5. Exit\n\n")
        user = int(input("Choose an option : "))
        if(user == 1):
            add_contacts(contacts)
        if(user == 2):
            show_contacts(contacts)
        if(user == 3):
            update_contacts(contacts)
        if(user == 4):
            remove_contact(contacts)
        if(user == 5):
            print("Exitin.....")
            break

        



def add_contacts(contacts):
    name = input("Enter name : ")
    phone = input("Enter phone number : ")
    email  = input("Enter email : ")
    contacts[name] = {
        'Phone': phone,
        'Email': email
    }
    print(f"Contact {name} has added successfully!")

def show_contacts(contacts):
    if not contacts:
        print("not found !")
    else:
        for name, details in contacts.items():
            print(f'name : {name}')
            print(f'Phone : {details["Phone"]}')
            print(f'Email {details["Email"]}')

def update_contacts(contacts):
        name = input("Enter the name you want to update : ")
        if name not in contacts:
            print("Not found !")
        else:
            phone = input("Enter new phone number :")
            email = input("Enter new email : ")
            contacts[name]={
                'Phone': phone,
                'Email': email
            }
        print("Contact has updated successfully!")

def remove_contact(contacts):
    name = input("Enter the name you want  to update : ")
    if name not in contacts:
        print("Not found !")
    else:
        del contacts[name]
    print("Contact has removed !")


main_m()