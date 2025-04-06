from student_management import add_student, view_students, update_student, delete_student


while True:
    print('\n----- Student Managament System ------')
    print("1. Add Student")
    print("2. View Students ")
    print("3. Update Student")
    print("4. Exit")

    choice  = int(input("Enter your choice : "))
    if choice == 1:
        name = input("Enter name : ")
        age = input("Enter age : ")
        gender = input("Enter phone : ")
        email = input("Enter email : ")
        phone = input("Enter phone : ")
        add_student(name, age, gender, email, phone)

    elif choice == 2:
        view_students()
    
    elif choice == 3:
        student_id = int(input("Enter student ID to update : "))
        name = input("Enter name")
        age = input("Enter age : ")
        gender = input("Enter phone : ")
        email = input("Enter email : ")
        phone = input("Enter phone : ")
        update_student(student_id, name, age, gender, email, phone)

    elif choice == 4:
        student_id = int(input("Enter student ID  to delete : "))
        delete_student(student_id)
    
    elif choice == 5:
        print("Exiting program....")
        break

    else:
        print("Invalid choice! ")
    