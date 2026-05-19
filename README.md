# 🎓 Centralized College Database Management System

A modern and responsive College Database Management System developed using **Flask**, **MySQL**, **HTML**, **CSS**, **Bootstrap**, and **JavaScript**.

This project helps manage:

- Students
- Instructors
- Courses
- Enrollment Records

through a clean web-based dashboard with CRUD operations and relational database integration.

---

# 🚀 Features

## 📊 Dashboard
- Institutional overview
- Total counts for:
  - Students
  - Courses
  - Instructors
  - Departments

---

## 👨‍🎓 Student Management
- Add students
- Delete students
- Search students instantly
- View student records

---

## 👨‍🏫 Instructor Management
- Add instructors
- Delete instructors
- Department dropdown selection
- Search instructors

---

## 📚 Course Management
- Add courses
- Delete courses
- Instructor dropdown selection
- Department dropdown selection
- Search courses

---

## 📝 Enrollment Management
- Enroll students into courses
- Delete enrollment records
- Student & course dropdowns
- Many-to-many relationship implementation

---

# 🛠️ Technologies Used


1. Flask ( Backend Framework )
2. MySQL ( Database )
3. HTML5 ( Structure ) 
4. CSS3 ( Styling )
5. Bootstrap 5 ( Responsive UI )
6. JavaScript ( Search Functionality )
7. Jinja2 ( Template Rendering )

---

# 🗂️ Project Structure

```bash
Centralized-College-Database/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── students.html
│   ├── instructors.html
│   ├── courses.html
│   ├── enrollment.html
│   └── add_student.html
│
├── app.py
├── database.sql
├── README.md
└── .gitignore
```

---

# 🧩 Database Design

## Tables Used

### 1. Department
Stores department information.

### 2. Student
Stores student details.

### 3. Instructor
Stores instructor details.

### 4. Courses
Stores course information.

### 5. Enrollment
Implements many-to-many relationship between:
- students
- courses

using foreign keys.

---

# 🔑 DBMS Concepts Implemented

- Primary Key
- Foreign Key
- CRUD Operations
- Relational Database
- Many-to-Many Relationship
- SQL Queries
- JOIN Operations
- Referential Integrity

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/rajpashwin-13/Centralized-College-Database.git
```

---

## 2️⃣ Open Project

```bash
cd Centralized-College-Database
```

---

## 3️⃣ Install Dependencies

```bash
pip install flask mysql-connector-python
```

---

## 4️⃣ Import Database

Open MySQL Workbench and run:

```sql
database.sql
```

---

## 5️⃣ Run Flask App

```bash
python app.py
```

---

## 6️⃣ Open Browser

```bash
http://127.0.0.1:5000
```

---

# 💡 Key Functionalities

✅ Responsive dashboard UI  
✅ Sidebar navigation  
✅ Flash messages  
✅ Search filtering  
✅ Dropdown-based forms  
✅ Relational database integration  
✅ CRUD functionality  

---

# 📷 Screenshots

## Dashboard


## Student Management


## Instructor Management


## Course Management


## Enrollment Management


---

# 👨‍💻 Developed By

- Ashwin Raj P
- Adithya N Poojari
- Ashin K
- Arjun Bhaskar


A J Institute of Engineering and Technology  
Department of CSE (AI & ML)

---

# 📄 License

This project is developed for educational and academic purposes.