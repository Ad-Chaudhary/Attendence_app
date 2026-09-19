import streamlit as st

st.title("Student Registration Form")
c1, c2,c3 = st.columns(3)
with st.form("enter your details"):
    name=c1.text_input("enter your name")
    age=c2.number_input("enter your age", min_value=1, max_value=100, step=1)
    photo=c3.file_uploader("upload your photo", type=["jpg","png"])




    filled= st.form_submit_button("submit your details")

if filled :
    st.success("your details submitted successfully")
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.image(photo ,width=200)