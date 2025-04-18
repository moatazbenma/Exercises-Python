from Connection_db import connect_db


class Student:
    def __init__(self, Nim, Full_Name, Departement, Faculty):
        self.Nim = Nim
        self.Full_Name = Full_Name
        self.Departement = Departement
        self.Faculty = Faculty

    def add_student(self):
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql = 'insert into student (Nim, Full_Name, Departement, Faculty) values(%s, %s, %s,%s)'
                values = (self.Nim, self.Full_Name, self.Departement, self.Faculty)
                cursor.execute(sql, values)
                db.commit()
                print('Student has added successfully !')
            except Exception as e:
                print(f'Error : {e}')
            finally:
                db.close()


    @staticmethod
    def view_student():
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql = 'SELECT * FROM student'
                cursor.execute(sql)
                student = cursor.fetchall()
                print('\n-----Student Records------')
                print("Nim--Full_name--Departement--Faculty")
                for students in student:
                    print(students)

            except Exception as e:
                print(f"Error : {e}")
            finally:
                db.close()



    def edit_student(self):
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql = 'UPDATE student SET Full_Name=%s, Departement=%s, Faculty=%s WHERE Nim=%s' 
                values = (self.Full_Name, self.Departement, self.Faculty, self.Nim)
                cursor.execute(sql, values)
                db.commit()
                print("Student has edited successfully !")
            except Exception as e:
                print(f"Error : {e}")
            finally:
                db.close()

    def delete_student(Nim):
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql = 'DELETE FROM student WHERE Nim= %s'
                values = (Nim,)
                cursor.execute(sql, values)
                db.commit()
                print("Student has deleted successfully !")
            except Exception as e:
                print(f"Error : {e}")
            finally:
                db.close()




class Subject:
    def __init__(self, subject_nm, Subject_name, Credit, Teacher):
        self.subject_nm = subject_nm
        self.Subject_name = Subject_name
        self.Credit = Credit
        self.Teacher = Teacher


    def add_subjects(self):
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql = 'INSERT INTO subjects (subject_nm, Subject_name, Credit, Teacher) VALUES (%s, %s, %s, %s)'
                values= (self.subject_nm, self.Subject_name, self.Credit, self.Teacher)
                cursor.execute(sql, values)
                db.commit()
                print("Subjects has added successfully !")
            except Exception as e:
                print(f"Error : {e}")
            finally: 
                db.close()

    def edit_subjects(self):
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql = 'UPDATE subjects SET Subject_name=%s, Credit=%s, Teacher=%s WHERE subject_nm=%s'
                values= (self.Subject_name, self.Credit, self.Teacher, self.subject_nm)
                cursor.execute(sql, values)
                db.commit()
                print("Subjects has added successfully !")
            except Exception as e:
                print(f"Error : {e}")
            finally: 
                db.close()

    def view_subjects():
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql = 'SELECT * FROM subjects'
                cursor.execute(sql)
                subject = cursor.fetchall()
                print('\n-----Subject Records------')
                for students in subject:
                    print(students)

            except Exception as e:
                print(f"Error : {e}")
            finally:
                db.close()
            
    def delete_subject(subject_nm):
        db = connect_db()
        if db:
            cursor = db.cursor()
            sql = "DELETE FROM subjects WHERE subject_nm= %s"
            values= (subject_nm,)
            cursor.execute(sql, values)
            db.commit()
            print("✅ Student deleted successfully!")
            db.close()

class Grade:
    def __init__(self, Nim, subject_nm, grade):
        self.Nim = Nim
        self.subject_nm = subject_nm
        self.grade = grade


    def add_grade(self):
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql = 'INSERT INTO grades(Nim, subject_nm, grade) VALUES (%s, %s, %s)'
                values = (self.Nim, self.subject_nm, self.grade)
                cursor.execute(sql, values)
                db.commit()
                print("✅ Student grade has been added")
            except Exception as e:
                print(f"Error : {e}")
            finally:
                db.close()

    @staticmethod
    def view_grade(Nim):
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql = 'SELECT * FROM grades WHERE Nim = %s'
                values = (Nim,)
                cursor.execute(sql, values)
                grades = cursor.fetchall()

                print('\n-----Grades Records------')
                for i in grades:
                    print(i)

            except Exception as e:
                print(f"Error : {e}")
            finally:
                db.close()
        
    def edit_grade(self):
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql= 'UPDATE grades SET subject_nm = %s, grade = %s WHERE Nim = %s'
                values = (self.subject_nm, self.grade, self.Nim)
                cursor.execute(sql, values)
                db.commit()
                print("✅ Student Grade has been Edited")
            except Exception as e:
                print(f"Error : {e}")
            finally: 
                db.close()


    @staticmethod
    def delete_grade(Nim):
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                sql = "DELETE FROM grades WHERE Nim = %s"
                values = (Nim,)
                cursor.execute(sql, values)
                db.commit()
                print("✅ Student Grade has been Deleted")
            except Exception as e:
                print(f"Error : {e}")
            finally:
                db.close()

