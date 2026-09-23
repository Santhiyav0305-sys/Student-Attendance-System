# Student Attendance System

A web-based Student Attendance Management System built using Python Flask and SQLite.

This application helps administrators manage students and teachers, mark daily attendance, view attendance history, view student profiles, and generate attendance reports.

## Project Overview

Student Attendance System is a Flask-based web application named AttendEase.

The system provides an admin portal to manage student records, teacher records, daily attendance, attendance history, student profiles, and reports.

## Features

### Admin Login

* Admin login authentication
* Secure session-based access
* Demo credentials for testing

### Dashboard

* Total students
* Total teachers
* Present attendance records
* Absent attendance records
* Overall attendance percentage
* Today's attendance statistics

### Student Management

* Add students
* View students
* Edit student details
* Delete students
* View individual student profiles

Student information includes:

* Full Name
* Email
* Department
* Phone

### Teacher Management

* Add teachers
* View teachers
* Edit teacher details
* Delete teachers

Teacher information includes:

* Full Name
* Email
* Subject

### Daily Attendance

* Select attendance date
* View all students
* Mark students as Present or Absent
* Save attendance
* Update existing attendance records
* Prevent duplicate attendance records

### Attendance History

* View attendance date
* View student name
* View department
* View attendance status

### Student Profile

* Student details
* Department
* Email
* Present count
* Absent count
* Attendance percentage
* Attendance history

### Attendance Reports

* Student name
* Department
* Total attendance records
* Present count
* Absent count
* Attendance percentage
* Print attendance reports

## Technologies Used

| Technology | Purpose             |
| ---------- | ------------------- |
| Python     | Backend programming |
| Flask      | Web framework       |
| SQLite     | Database            |
| HTML       | Web page structure  |
| CSS        | Styling             |
| JavaScript | UI behavior         |
| Jinja2     | Template rendering  |

## Project Structure

Student-Attendance-System/

```
OnlineAttendanceSystem/
    app.py
    database.db
    requirements.txt
    static/
        script.js
        style.css
        images/
    templates/
        about.html
        add_student.html
        add_teacher.html
        attendance.html
        attendance_history.html
        base.html
        dashboard.html
        edit_student.html
        edit_teacher.html
        login.html
        reports.html
        student_profile.html
        students.html
        teachers.html
```

## Installation and Execution

### Step 1: Install Python

Check Python installation:

```
python --version
```

### Step 2: Clone Repository

```
git clone https://github.com/Santhiyav0305-sys/Student-Attendance-System.git

cd Student-Attendance-System

cd OnlineAttendanceSystem
```

### Step 3: Create Virtual Environment

Windows:

```
python -m venv venv
```

Linux / macOS:

```
python3 -m venv venv
```

### Step 4: Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

Linux / macOS:

```
source venv/bin/activate
```

### Step 5: Install Dependencies

```
pip install -r requirements.txt
```

### Step 6: Run Application

```
python app.py
```

### Step 7: Open Application

```
http://127.0.0.1:5000
```

## Demo Login

Username: admin

Password: admin123

Note: Demo credentials are used for testing purposes. Production applications should use secure authentication and password hashing.

## Database

The project uses SQLite for data storage.

Database file:

```
database.db
```

Main tables:

* Students
* Teachers
* Attendance

Attendance records include student ID, date, and status.

## Application Flow

Admin Login → Dashboard → Student Management → Teacher Management → Daily Attendance → Attendance History → Reports

## Learning Outcomes

This project helps develop practical knowledge in:

* Python programming
* Flask web development
* SQLite database operations
* CRUD operations
* HTML and CSS
* JavaScript
* Jinja2 templates
* Sessions and authentication
* Database relationships
* Attendance calculations
* Git and GitHub

## Future Improvements

* Secure password hashing
* Teacher login
* Student login
* Stronger form validation
* Monthly attendance reports
* Export reports to CSV/PDF
* REST API
* Cloud database
* Automated testing
* Production deployment

## Author

### Santhiya V

M.Sc. Information Technology Student

Tamil Nadu, India

LinkedIn: https://www.linkedin.com/in/santhiya-veerapathiran-7a50b2344

GitHub: https://github.com/Santhiyav0305-sys

## Project Goal

The goal of this project is to provide a simple web-based solution for managing students, teachers, daily attendance, attendance history, and attendance reports.

Technologies: Python, Flask, SQLite, HTML, CSS, JavaScript, and GitHub.

Thank you for visiting the Student Attendance System project!
