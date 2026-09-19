import mysql.connector
import streamlit as st
import pandas as pd

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Delhi@123",
    database="crud"
)
st.title("Data Visualization")
workspace = st.sidebar.selectbox("Choose Your Workspace", ["Branch", "Gender", "Attendance"])
st.write(f"You have selected {workspace} workspace")
cur=conn.cursor()
q="select* from student"
cur.execute(q)
data=cur.fetchall()

df=pd.DataFrame(data)
st.write(df)

