import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
from datetime import date

# Database connection
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Delhi@123",
    database="crud"
)

#Login session state management
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "role" not in st.session_state:
    st.session_state["role"] = ""
if "full_name" not in st.session_state:
    st.session_state["full_name"] = ""

def authenticate_user(username, password):
    cur = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cur.execute(query, (username, password))
    user = cur.fetchone()
    return user

def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.session_state["role"] = ""
    st.session_state["full_name"] = ""
    st.rerun()

if not st.session_state["logged_in"]:
    st.title("Student Attendance System")
    st.subheader("Login to access your workspace")
    
    with st.form("login_form"):
        username_input = st.text_input("Username")
        password_input = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            user = authenticate_user(username_input, password_input)
            if user:
                st.session_state["logged_in"] = True
                st.session_state["username"] = user["username"]
                st.session_state["role"] = user["role"]
                st.session_state["full_name"] = user["full_name"]
                st.success(f"Welcome, {user['full_name']}!")
                st.rerun()
            else:
                st.error("Invalid Username or Password.")
    st.stop()


st.sidebar.markdown(f"**Logged in as:** {st.session_state['full_name']}")
st.sidebar.markdown(f"**Role:** `{st.session_state['role']}`")
st.sidebar.button("Logout", on_click=logout)
st.sidebar.divider()

st.title("Students Attendance System")
workspace = st.sidebar.selectbox("Choose Your Workspace", ["Attendance Marking","Attendance Status","Add New Student","Delete Student","Update Attendance"])
st.write(f"You have selected {workspace} workspace")
cur=conn.cursor()


#Workspace: Attendance Marking
if workspace == "Attendance Marking":
    st.subheader("Mark Daily Attendance")
    today = date.today()
    selected_date = st.date_input(
        "Select Date", 
        value=today, 
        max_value=today,
        help="You cannot mark attendance for future dates."
    )
    
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT student_id, roll_no, student_name, department FROM students")
    students = cur.fetchall()
    
    if students:
        with st.form("attendance_form"):
            attendance_records = {}
            st.write("Check box if student is **Present**:")
            
            for student in students:
                is_present = st.checkbox(
                    f"{student['roll_no']} | {student['student_name']} ({student['department']})", 
                    key=f"std_{student['student_id']}"
                )
                attendance_records[student['student_id']] = "Present" if is_present else "Absent"
            
            submit_attendance = st.form_submit_button("Submit Attendance")
            
            if submit_attendance:
                insert_query = """
                    INSERT INTO attendance (student_id, attendance_date, status)
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE status = VALUES(status)
                """
                payload = [(s_id, selected_date, status) for s_id, status in attendance_records.items()]
                
                cur.executemany(insert_query, payload)
                conn.commit()
                st.success(f"Attendance recorded successfully for {selected_date}!")
    else:
        st.info("No students found in the database. Please add students first.")

#Workspace: Add New Student
elif workspace=="Add New Student":
   st.subheader("Add New Student Details")

   with st.form("enter your details"):
    student_id=st.number_input("Enter Student_id")
    roll_no=st.number_input("Enter Student Roll Number")
    student_name=st.text_input("Enter Student Name")
    department=st.selectbox("Departmet",["CSE","AI","IT"])

    submitted=st.form_submit_button("Save Data")

    cur=conn.cursor()
    if submitted:
       if student_name.strip():
        Query=""" insert into students(student_id,roll_no,student_name,department)
        values(%s,%s,%s,%s)"""
        cur.execute(Query,(student_id,roll_no,student_name,department))
        conn.commit()
        st.success("Data saved successfully!")
    else:
        st.warning("Please enter a valid Name.")

        q="select* from students"
        cur.execute(q)
        data=cur.fetchall()

        df=pd.DataFrame(data)
        st.write(df)

#Workspace: Delete Student
elif workspace=="Delete Student":
   st.subheader("Delete Student Details")
   student_id=st.number_input("Enter Student_id to delete")
   if st.button("Delete Student"):
    cur=conn.cursor()
    Query=""" delete from students where student_id=%s"""
    cur.execute(Query,(student_id,))
    conn.commit()
    st.success("Student deleted successfully!")

#Workspace: Attendance Status
elif workspace == "Attendance Status":
    st.subheader("Attendance Status")
    
    tab1, tab2 = st.tabs(["Daily Records", "Low Attendance Alert (<75%)"])
    cur = conn.cursor(dictionary=True)
    
    with tab1:
        view_date = st.date_input("Filter by Date")
        query = """
            SELECT s.roll_no, s.student_name, s.department, a.status 
            FROM attendance a
            JOIN students s ON a.student_id = s.student_id
            WHERE a.attendance_date = %s
        """
        cur.execute(query, (view_date,))
        data = cur.fetchall()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.warning("No records found for this date.")
            
    with tab2:
        agg_query = """
            SELECT 
                s.roll_no, 
                s.student_name, 
                s.department,
                COUNT(a.attendance_id) AS total_classes,
                SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) AS attended_classes,
                ROUND((SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) / COUNT(a.attendance_id)) * 100, 2) AS percentage
            FROM students s
            LEFT JOIN attendance a ON s.student_id = a.student_id
            GROUP BY s.student_id
            HAVING percentage < 75 OR total_classes = 0
        """
        cur.execute(agg_query)
        low_att_df = pd.DataFrame(cur.fetchall())
        st.dataframe(low_att_df, use_container_width=True)

#Workspace: Update Attendance
elif workspace == "Update Attendence":
    st.subheader("Update Attendance Record")
    
    update_date = st.date_input("Select Date to Modify")
    cur = conn.cursor(dictionary=True)
    
    cur.execute("""
        SELECT a.attendance_id, s.  roll_no, s.student_name, a.status 
        FROM attendance a 
        JOIN students s ON a.student_id = s.student_id 
        WHERE a.attendance_date = %s
    """, (update_date,))
    
    records = cur.fetchall()
    
    if records:
        student_dict = {f"{r['roll_no']} - {r['student_name']} (Current: {r['status']})": r for r in records}
        selected_student = st.selectbox("Select Student Record", list(student_dict.keys()))
        new_status = st.selectbox("New Status", ["Present", "Absent"])
        
        if st.button("Update Record"):
            target_record = student_dict[selected_student]
            cur.execute(
                "UPDATE attendance SET status = %s WHERE attendance_id = %s",
                (new_status, target_record['attendance_id'])
            )
            conn.commit()
            st.success("Record updated successfully!")
    else:
        st.info("No attendance records found for the selected date.")

elif workspace == "Update Attendance":
    st.subheader("Update Attendance Record")
    
    update_date = st.date_input("Select Date to Modify")
    cur = conn.cursor(dictionary=True)
    
    cur.execute("""
        SELECT a.attendance_id, s.roll_no, s.student_name, a.status 
        FROM attendance a 
        JOIN students s ON a.student_id = s.student_id 
        WHERE a.attendance_date = %s
    """, (update_date,))
    
    records = cur.fetchall()
    
    if records:
        student_dict = {f"{r['roll_no']} - {r['student_name']} (Current: {r['status']})": r for r in records}
        selected_student = st.selectbox("Select Student Record", list(student_dict.keys()))
        new_status = st.selectbox("New Status", ["Present", "Absent"])
        
        if st.button("Update Record"):
            target_record = student_dict[selected_student]
            cur.execute(
                "UPDATE attendance SET status = %s WHERE attendance_id = %s",
                (new_status, target_record['attendance_id'])
            )
            conn.commit()
            st.success("Record updated successfully!")
    else:
        st.info("No attendance records found for the selected date.")

#End of the application

   








  


    
