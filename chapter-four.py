import streamlit as st
import pandas as pd

file = st.file_uploader("Choose a file: ", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.subheader("Course Sales Data Preview")
    st.dataframe(df)

if file is not None:
    st.subheader("Sales Summary Stats: ")
    st.write(df.describe())
if file is not None:
    cities = df["city"].unique()
    selected_city = st.selectbox("Select city: ", cities)
    selected_unique_city_df = df[df["city"] == selected_city]
    st.dataframe(selected_unique_city_df)