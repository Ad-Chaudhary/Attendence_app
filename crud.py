import mysql.connector
import streamlit as st
import pandas as pd

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Delhi@123",
    database="crud"
)

st.title("Data Collection Form")
with st.form("Create Data"):
    name=st.text_input("Name")
    gender=st.selectbox("Gender",["Male","Female"])
    department=st.selectbox("Departmet",["CSE","AI","IT"])
    marks=st.number_input("Enter Marks",step=1)
    attandence=st.number_input("Enter Attandence",step=1)

    submitted=st.form_submit_button("Save Data")

cur=conn.cursor()
if submitted:
    if name.strip():
        Query=""" insert into student(name,gender,department,marks,attandence)
        values(%s,%s,%s,%s,%s)"""
        cur.execute(Query,(name,gender,department,marks,attandence))
        conn.commit()
        st.success("Data saved successfully!")
    else:
        st.warning("Please enter a valid Name.")




q="select* from student"
cur.execute(q)
data=cur.fetchall()

df=pd.DataFrame(data)
st.write(df)
