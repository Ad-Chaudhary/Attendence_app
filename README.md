Student Attendance System
A lightweight Streamlit app for managing student profiles and tracking daily attendance using MySQL.

Features
Authentication: Login interface with session management.

Attendance Marking: Select dates and mark present/absent statuses.

Reports & Analytics: Daily attendance records and low-attendance alerts (<75%).

Student Management: Add and delete student records.

Record Updates: Modify existing attendance logs for any given date.

Tech Stack
Frontend/App: Streamlit

Data Processing: Pandas, NumPy

Database: MySQL (mysql-connector-python)

Setup & Running
Install Dependencies:

Bash
pip install streamlit pandas numpy mysql-connector-python
Configure Database:
Update the MySQL credentials in app.py:

Python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="crud"
)
Run App:

Bash
streamlit run app.py