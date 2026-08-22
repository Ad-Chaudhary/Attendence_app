import streamlit as st
import pandas as pd


st.title("Student Performance Dashboard")
col1, center_col, col3 = st.columns([1, 2, 1])
f = center_col.file_uploader("Upload your file", type=["xlsx", "xls", "csv"])

if f is not None:
    if f.name.endswith(".csv"):
        df = pd.read_csv(f)
    else:
        df = pd.read_excel(f)
    st.dataframe(df)
    total_students = df.shape[0]
    avg_marks = round(df["Marks"].mean(), 2)
    avg_attendance = round(df["Attendance"].mean(), 2)
    high_marks = df["Marks"].max()
    lowest_marks = df["Marks"].min()

    if st.checkbox("Show details"):
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Students:", total_students)
        c2.metric("Average Marks:", avg_marks)
        c3.metric("Average Attendance:", f"{avg_attendance}%")

    available_depts = df["Department"].unique().tolist()
    Dept = st.multiselect(
        "Department", options=available_depts, default=available_depts
    )
    if Dept:
        st.write(df[df["Department"].isin(Dept)])

    min_val = int(df["Marks"].min())
    max_val = int(df["Marks"].max())
    m = st.slider(
        "Choose Marks (Maximum Threshold)",
        min_value=min_val,
        max_value=max_val,
        value=max_val,
        step=10,
    )
    st.write(df[df["Marks"] <= m])


    c4, c5 = st.columns(2)
    with c4:
        if st.checkbox("Highest Marks"):
            st.write(df[df["Marks"] == high_marks])
    with c5:
        if st.checkbox("Lowest Marks"):
            st.write(df[df["Marks"] == lowest_marks])

else:
    st.info("Please upload an Excel or CSV file to display the dashboard.")