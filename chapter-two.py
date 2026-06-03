import streamlit as st

st.title("Data Science Learning App")
if st.button("Start Learning"):
    st.success("Your learning is start.")

chapter_1 = st.checkbox("Chapter-1")
if chapter_1:
    st.write("Chapter-1 completed!")

teaching_quality = st.radio("Teaching quality of the mentor: ", ["fine", "Excellent!", "Need to improve" ])

ratings = st.selectbox("Your ratings for this chapter: ", ["⭐⭐⭐⭐⭐","⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐"])
caring_level_of_mentor = st.slider("Mentor's caring level while teaching students: ", 0,5,2)

st.subheader("Taking inputs from users: ")

practiced_day = st.number_input("How many days you've practiced in this month?", min_value=1, max_value=30, step=1)

st.write(f"you've practiced: {practiced_day} days in this month.")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Congratulations! {name} you're on the right way of becoming a Data Scientist!")

date_watching = st.date_input("Select the date you're watching the tutorial: ")
st.write(f"Your watching date is: {date_watching}")