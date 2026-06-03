import streamlit as st
import pandas as pd

st.title("Hello from Data Science Academy!")
st.subheader("Brewed with Data")
st.text("Weclocme to your first interactive lms dashboard!")
st.write("Choose your favourite domain")

domain = st.selectbox("Your favourite domain: ", ["Data Science", "Machine Learning", "AI Generalist", "AI Builders"])
st.write(f"You choose {domain}. Excellent choice!")
st.success("Your domain is selectedt. Now you're ready to learn.")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': ["Rakesh", "Rafi", "Mohit", "Sujata"]
}))

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

