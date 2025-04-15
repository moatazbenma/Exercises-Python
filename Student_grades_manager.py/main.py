from Student_grades import Student, Subject

def main():
    while True:
        print("\nMade By : MTZ_BNS\n")
        print("1. Student")
        print("2. Subjects")
        print("3. Exit")

        try:
            user = int(input("Enter Your Choice : "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        if user == 1:
            student_menu()
        elif user == 2:
            subject_menu()
        elif user == 3:
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid option. Try again.")

def student_menu():
    print("\n--- Student Menu ---")
    print("1. Add Student")
    print("2. View Student")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Return Back")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Invalid input.")
        return

    if choice == 1:
        Nim = int(input("Nim: "))
        Full_Name = input("Full Name: ")
        Departement = input("Departement: ")
        Faculty = input("Faculty: ")

        student = Student(Nim, Full_Name, Departement, Faculty)
        student.add_student()

    elif choice == 2:
        Student.view_student()

    elif choice == 3:
        Nim = int(input("Nim: "))
        Full_Name = input("Full Name: ")
        Departement = input("Departement: ")
        Faculty = input("Faculty: ")

        student = Student(Nim, Full_Name, Departement, Faculty)
        student.edit_student()

    elif choice == 4:
        Nim = int(input("Nim: "))
        Student.delete_student(Nim)

    elif choice == 5:
        return

    else:
        print("❌ Invalid option.")

def subject_menu():
    print("\n--- Subject Menu ---")
    print("1. Add Subject")
    print("2. Edit Subject")
    print("3. View Subject")
    print("4. Delete Subject")
    print("5. Return Back")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Invalid input.")
        return

    if choice == 1:
        subject_nm = input("Subject Number: ")
        subject_Name = input("Subject Name: ")
        Credit = input("Credit: ")
        Teacher = input("Teacher: ")

        subject = Subject(subject_nm, subject_Name, Credit, Teacher)
        subject.add_subjects()

    elif choice == 2:
        subject_nm = input("Subject Number: ")
        subject_Name = input("Subject Name: ")
        Credit = input("Credit: ")
        Teacher = input("Teacher: ")

        subject = Subject(subject_nm, subject_Name, Credit, Teacher)
        subject.edit_subjects()

    elif choice == 3:
        Subject.view_subjects()

    elif choice == 4:
        subject_nm = input("Subject Number: ")  
        Subject.delete_subject(subject_nm)

    elif choice == 5:
        return

    else:
        print("❌ Invalid option.")

main()
