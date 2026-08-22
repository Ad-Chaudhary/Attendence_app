import streamlit as st
import pandas as pd

st.title("Student Performance Dashboard")
col1, center_col, col3 = st.columns([1, 2, 1])
f=center_col.file_uploader("Upload your file")
if f is not None:
    df=pd.read_excel(f)
    st.dataframe(df)

total_students=df.shape[0]
avg_marks=df["Marks"].mean()
avg_attendance=df["Attendance"].mean()
high_marks=df["Marks"].max()
lowest_marks=df["Marks"].min()

if st.checkbox("Show deatails"):
    c1,c2,c3=st.columns(3)
    c1.metric("Total Students:", total_students)
    c2.metric("Average Marks:", avg_marks)
    c3.metric("Average Attendance:", avg_attendance)

Dept=st.multiselect("Department", ["CSE", "IT", "AI"])
st.write(df[df["Department"].isin(Dept)])

m=st.slider("Choose Marks",step=10)
st.write(df[df["Marks"] <= m])

c4,c5=st.columns(2)
with c4:
    if st.checkbox("Highest Marks"):
        st.write(df[df["Marks"]==high_marks])
with c5:
    if st.checkbox("Lowest Marks"):
        st.write(df[df["Marks"]==lowest_marks])



