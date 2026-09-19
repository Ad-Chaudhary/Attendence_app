import pandas as pd
import streamlit as st
import numpy as np


st.title("DATA CLEANING")

uploaded_file = st.file_uploader("Upload a CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Original Dataset")
    st.dataframe(df)

    # Checkboxes
    remove_duplicates = st.checkbox("Remove Duplicate Rows")
    remove_missing = st.checkbox("Remove Missing Values")

    # Create a copy so original data remains unchanged
    cleaned_df = df.copy()

    if remove_duplicates:
        cleaned_df = cleaned_df.drop_duplicates()

    if remove_missing:
        cleaned_df = cleaned_df.dropna()

    # Show cleaned data only if at least one option is selected
    if remove_duplicates or remove_missing:

        st.subheader("Cleaned Dataset")
        st.dataframe(cleaned_df)

        st.subheader("Dataset Information")
        st.write("Rows:", cleaned_df.shape[0])
        st.write("Columns:", cleaned_df.shape[1])

        csv = cleaned_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download Cleaned Dataset",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )



