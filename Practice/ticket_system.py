more_than_3 = []
less_than_3 = []

viewer_count = 0


def main():
    while True:
        print("1. Add ticket")
        print("2. View ticket")
        print("3. Exit")



        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print('Please enter a valid number')
            continue

        if choice == 1:
            add_ticket()

        elif choice == 2:
            view_ticket()

        elif choice == 3:
            print("Exiting....")
            break

def add_ticket():
    global viewer_count

    if viewer_count >= 5:
        print('Maximum number of viewers reacher')
        return
    
    viewer = input("Enter The name of viewer : ")
    age = int(input("Enter your age : "))



    if age < 3:
        print("The ticket is free for you !")
        less_than_3.append(viewer)

    else:
        more_than_3.append(viewer)
        print("Ticket has added successfully!")
        print("The ticket price is 30,000")
        
    
    viewer_count += 1


def view_ticket():
    total = 0
    for i in more_than_3:
        print(f" Viewer : {i}")
        print(f"Price : 30,000")
        total += 30000

    print("-----------------------")

    for i in less_than_3:
        print(f" Viewer : {i}")
        print(f"Price : free")
    

    print("------------------------")
    print(f"Total : {total}")

main()