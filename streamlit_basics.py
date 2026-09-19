import streamlit as st
import pandas as pd
import numpy as np

# st.title("Hello Hi......")
# st.subheader("i am adarsh")
# st.text("this is my first streamlit app")
# st.write("this the streamlit app for the first time")

# color = st.selectbox("select your favorite color", ["red", "green", "blue", "yellow"])
# st.write(f"Your favorite color is {color}")

# st.success("color selected successfully")

# st.title("Chai Maker app")
# if st.button("Make Chai"):
#     st.sucess("Chai is being made...")
#     st.balloons()

# add_masala = st.checkbox("Add Masala")

# if add_masala:
#     st.write("Masala added to your chai")

# tea_type = st.radio("select your material", ["milk","water"])
# st.write(f"seleceted material is {tea_type}")

# flavour=st.selectbox("choose flavour", ["ginger","cardamom","tulsi"])
# st.write(f"seleceted flavour is {flavour}")

# sugar=st.slider("select your sugar spoon", 0, 10, 5)
# st.write(f"selected sugar spoon is {sugar}")

# cups=st.number_input("slect number of cups", min_value=1,max_value=10, value=1, step=1)
# st.write(f"number of cups selected ={cups}")

# name=st.text_input("enter your name")
# if name:
#     st.write(f"Hello {name}, your chai is ready!")


# st.title("chai taste poll")
# col1,col2=st.columns(2)

# with col1:
#     st.header ("Adark chai")
#     st.image("https://imgs.search.brave.com/pwOPqRei1L9pAr5YAZcW2sY1oCNJgTB8JmF4TUQaLBs/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzE5LzAxLzgyLzcy/LzM2MF9GXzE5MDE4/MjcyNDdfMWVFeUlQ/VDZTMGJ5V0VwWWFI/eVlDWTRBSTVGb0Fu/NnEuanBn", width =200)
#     vote1=st.button(" vote for Adark chai")

# with col2:
#     st.header("masla chai")
#     st.image("https://imgs.search.brave.com/5pX0QBa-zsdORxfskNHQMC9oy2h7WqImIryQfz95Xqk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/bWFnbmlmaWMuY29t/L3ByZW1pdW0tcHNk/L3Rhc3R5LWluZGlh/bi1tYXNhbGEtY2hh/aS1pc29sYXRlZC10/cmFuc3BhcmVudC1i/YWNrZ3JvdW5kXzkx/ODA0OS0yNzg4Lmpw/Zz9zZW10PWFpc19o/eWJyaWQmdz03NDAm/cT04MA", width=200)
#     vote2=st.button("vote for masala chai")

# if vote1:
#     st.success("thanks for voting Adark chai")
# elif vote2:
#     st.success("thanks for voting masala chai")

# side=st.sidebar.text_input("input your name ")
# tea=st.sidebar.selectbox("choose your chai",["masala","adark"])
# st.write(f"Welcome {side} and your {tea} is getting ready")

# with st.expander("see your order"):
#     st.write(f"your order is {tea} and your name is {side}")

# st.title("Student Attendence Dashboard")

# file=st.file_uploader("Upload your csv file",type=["csv"])

# if file:
#     df=pd.read_csv(file)
#     st.subheader("Data Preview")
#     st.dataframe(df)

# if file:
#     st.subheader("Summary Stats")
#     st.write(df.describe())

import requests
st.title("Live Currency Converter")
amount = st.number_input("Enter the amount in INR", min_value=1)
target_currency=st.selectbox("Convert to -", ["USD", "EUR", "GBP", "JPY"])
if st.button("Convert"):
    url=f"https://api.exchangerate-api.com/v4/latest/INR"
    response=requests.get(url)

    if response.status_code==200:
        data=response.json()
        exchange_rate=data["rates"][target_currency]
        converted_amount=amount*exchange_rate
        st.success(f"{amount} INR = {converted_amount:.2f} {target_currency}")
    else:
        st.error("Error fetching exchange rates. Please try again later.")
        



