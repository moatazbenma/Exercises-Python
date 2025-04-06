import mysql.connector
import config

try:
    mydb = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)
    print("Data base has connected successfully")

except mysql.connector.Error as e:
    print("Error connecting to mysql", e)

my_cursor = mydb.cursor()



def main():
    while True:
        print("1. Add New Employee")
        print("2. Search Employee")
        print("3. Edit Employee")
        print("4. Delete Employee")
        print("5. Exit")


        user = int(input("Enter your choice : "))



def add_employee():
    id = int(input("Enter The Id : "))
    name = input("Enter The Full Name : ")
    age = int(input("Enter the age : "))
    salary = int(input("Enter the salary : "))

    sql = "INSERT INTO employee (id, name, age, salary) VALUES (%s, %s, %s, %s)"
    values = (id, name, age, salary)
    try:
        my_cursor.execute(sql, values)
        mydb.commit()
        print("Student has added succesfully ! ")
    except Exception as e:
        print("Error: ", e)
        mydb.rollback()
                            
 


def search_employee():
    id = input("Enter the id of the employer : ")
    sql = 'SELECT * from employee WHERE id = %s'
    Values = (id,)
    
    try:
        my_cursor.execute(sql, Values)
        result = my_cursor.fetchone()
        mydb.commit()
        if result:
            print("Employee found : ", result)
        else:
            print("No Employee Found ! ")



    except Exception as e:
        print("Error : ", e)
        mydb.rollback()


def edit_employee():
    id = input("Enter the id : ")
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    salary = int(input("Enter salary : "))

    sql = 'UPDATE employee SET name = %s, age = %s, salary = %s WHERE id = %s'
    values = (name, age, salary, id)
    try:
        my_cursor.execute(sql, values)
        mydb.commit()
    except Exception as e:
        print("Error ", e)
        mydb.rollback()






def delete_employee():
    id = input("Enter your id : ")


    check_sql = 'SELECT * from employee WHERE id = %s'
    values = (id,)
    my_cursor.execute(check_sql, values)
    result = my_cursor.fetchone()
        
    if result:
        sql = 'DELETE from employee WHERE id = %s'
        try:
            my_cursor.execute(sql, values)
            mydb.commit()
            print("Employee deleted successfully !")
        except Exception as e:
            print("Error : ", e)
            mydb.rollback()
    
    else:
        print(f"No employee found with ID {id}. Deletion failed.")

    






def mydb_connection():
    mydb.close()
    print("Database connection closed !")