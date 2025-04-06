students = []





def add_student():
    nim = input("Enter Your Nim : ")
    name = input("Enter Your Name : ")
    course = input("Enter Course : ")

    students.append({'nim': nim, 'name': name, 'course': course})
    print("Student has been added successfully! \n")


def view_student():
    if not  students:
        print('No Data ! \n')
        return
    
    else:
        print("List of Students : ")
        for student in students:
            print(f"Nim : {student['nim']}, Name : {student['name']}, Course: {student['course']} \n")

def search_student():
    if not students:
        print("No data yet!")
        return

    else:
        search = input("Enter the nim of student : ")
        for student in students:
            if student['nim'] == search:
                print(f"Found Student, Nim : {student['nim']}, Name: {student['name']}, Course : {student['course']}")
                return

        print("Student Not Found ! \n")


def update_student():
    if not students:
        print("No data yet !")
        return
    
    else:
        nim = input("Enter the NIM of the student to update : ")
        for student in students:
            if student['nim'] == nim:
                student['name'] = input("Enter new name : ")
                student['course'] = input("Enter new course : ")
                print("data has updated succesffuly! ")
                return

    print("Student Not Found \n")

def delete_student():
    if not students:
        print("No data yet !")
        return
    else:
        delete = input("Enter the nim to delete the student : ")
        for student in students:
            if delete == student['nim']:
                students.remove(student)
                print("Data has been removed successfully ! ")
                return

    print("Student Not Found \n")



def main(): 
    while True:
        print("1. Add Student")
        print("2. View Students ")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit\n\n")


        try:
            user = int(input("Enter your choice : "))
        except ValueError:
            print("Invalid input! Please enter a number between 1-6 \n")
            continue

        if user == 1:
            add_student()

        elif user == 2:
            view_student()

        elif user == 3:
            search_student()

        elif user == 4:
            update_student()


        elif user == 5:
            delete_student()

        elif user == 6:
            print("good bye !")
            break

        else:
            print("Invalid number !")
            return






main()






