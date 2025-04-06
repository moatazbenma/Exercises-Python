tasks = []

while True:
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option : ")
    if choice == '1':
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}\n\n")
        

    elif choice == '2':
        task = input("Enter a new task : ")
        tasks.append(task)
        print("Task Added!")

    elif choice == '3':
        if not tasks:
            print("No tasks to remove!")
        else:
            try:
                num = int(input("Enter task number to remove : "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Enter a valid number !")
    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again")
    
    


