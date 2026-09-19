import streamlit as st
import pandas as pd

# Page title
st.title("Student Performance Dashboard")

# Read CSV file
df = pd.read_csv("student_performance.csv")

# Display complete dataset
st.header("Complete Student Dataset")
st.dataframe(df)

# Basic statistics
st.header("Student Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", len(df))

with col2:
    st.metric("Average Marks", round(df["Marks"].mean(), 2))

with col3:
    st.metric("Average Attendance", round(df["Attendance"].mean(), 2))


# Department filter
st.header("Filter Students")

departments = ["All"] + sorted(df["Department"].unique().tolist())

selected_department = st.selectbox(
    "Select Department",
    departments
)

# Minimum marks filter
min_marks = st.slider(
    "Select Minimum Marks",
    min_value=int(df["Marks"].min()),
    max_value=int(df["Marks"].max()),
    value=int(df["Marks"].min())
)

# Attendance filter
attendance_filter = st.checkbox(
    "Show only students with attendance 75% or above"
)

# Apply department filter
filtered_df = df.copy()

if selected_department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == selected_department
    ]

# Apply marks filter
filtered_df = filtered_df[
    filtered_df["Marks"] >= min_marks
]

# Apply attendance filter
if attendance_filter:
    filtered_df = filtered_df[
        filtered_df["Attendance"] >= 75
    ]


# Display filtered data
st.subheader("Filtered Student Data")
st.dataframe(filtered_df)


# Highest and lowest marks
if len(filtered_df) > 0:
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Highest Marks",
            filtered_df["Marks"].max()
        )

    with col2:
        st.metric(
            "Lowest Marks",
            filtered_df["Marks"].min()
        )
else:
    st.warning("No students match the selected filters.")


# Download filtered data
csv_data = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Data",
    data=csv_data,
    file_name="filtered_student_performance.csv",
    mime="text/csv"
)


# Chart: Average marks by department
st.header("Average Marks by Department")

avg_marks = df.groupby("Department")["Marks"].mean()

st.bar_chart(avg_marks)