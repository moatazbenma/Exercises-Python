from db_connection import connect_db


def add_student(name, age, gender, email, phone):
    db = connect_db()
    if db:
        cursor = db.cursor()
        sql = "INSERT INTO students (name, age, gender, email, phone) VALUES (%s, %s, %s, %s, %s)"
        values = (name, age, gender, email, phone)
        cursor.execute(sql, values)
        db.commit()
        print("✅ Student added successfully!")
        db.close()

def view_students():
    db = connect_db()
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        print('\n-----Student Records------')
        for student in students:
            print(student)
        db.close()


def update_student(student_id, name, age, gender, email, phone):
    db = connect_db()
    if db:
        cursor = db.cursor()
        sql = "UPDATE students SET name=%s, age=%s, gender=%s, email=%s, phone=%s WHERE student_id=%s"
        values = (name, age, gender, email, phone, student_id)
        cursor.execute(sql, values)
        db.commit()
        print("✅ Student updated successfully!")
        db.close()

def delete_student(student_id):
    db = connect_db()
    if db:
        cursor = db.cursor()
        sql = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(sql, (student_id,))
        db.commit()
        print("✅ Student deleted successfully!")
        db.close()


