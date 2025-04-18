# 🎓 Student Grades Management System

A simple and functional CLI-based system built in **Python** and **MySQL** to manage Students, Subjects, and Grades using Object-Oriented Programming (OOP) principles.

---

# 🎓 Student Grades Management System

A simple and functional CLI-based system built in **Python** and **MySQL** to manage Students, Subjects, and Grades using Object-Oriented Programming (OOP) principles.

---

## 📌 Features

- ✅ Add, View, Edit, Delete **Students**
- ✅ Add, View, Edit, Delete **Subjects**
- ✅ Add, View, Edit, Delete **Grades**
- ✅ View grades per student
- ✅ Structured, modular code using OOP
- ✅ Proper use of database relationships and foreign keys
- ✅ Clear, navigable menu for user interaction

---

## 🧠 Tech Stack

- **Language:** Python 3
- **Database:** MySQL
- **Libraries:** `mysql-connector-python`

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/moatazbenma/student-grades-system.git
cd student-grades-system


## 2. Install dependencies
```bash
pip install mysql-connector-python



### 3. Create your MySQL database and tables
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE student (
  Nim INT PRIMARY KEY,
  Full_Name VARCHAR(255),
  Departement VARCHAR(255),
  Faculty VARCHAR(255)
);

CREATE TABLE subjects (
  subject_nm INT PRIMARY KEY,
  Subject_name VARCHAR(255),
  Credit VARCHAR(10),
  Teacher VARCHAR(255)
);

CREATE TABLE grades (
  Nim INT,
  subject_nm INT,
  grade VARCHAR(10),
  FOREIGN KEY (Nim) REFERENCES student(Nim),
  FOREIGN KEY (subject_nm) REFERENCES subjects(subject_nm)
);



### 4.Run the application
python main.py



# 🚀 What I Learned

- Structuring a project using Object-Oriented Programming
- Using MySQL with Python and managing relationships via foreign keys
- Handling user input, validation, and error messages
- Creating reusable and readable code

---

## 🙌 Acknowledgements

Built with passion and curiosity by **MTZ_BNS** 💻  
Feel free to fork, contribute, or provide feedback!

---

## 📬 Contact

- **LinkedIn:** [el-mouataz-benmanssour](https://www.linkedin.com/in/el-mouataz-benmanssour-b427a1318/)
- **GitHub:** [moatazbenma](https://github.com/moatazbenma)
