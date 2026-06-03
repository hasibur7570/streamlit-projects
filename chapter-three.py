import streamlit as st

st.title("Streamlit Columns Example")

col1, col2 = st.columns(2)

with col1:
    st.image("https://cdn.prod.website-files.com/63ccf2f0ea97be12ead278ed/644a18b637053fa3709c5ba2_what-is-data-science.jpg", width=200)
    st.header("Data Science Live Batch")
    st.write("You will learn live from the mentor")
    if st.button("Enroll Live Batch"):
        st.success("Enroll successfull to Live Batch")

with col2:
    st.image("https://www.fsm.ac.in/blog/wp-content/uploads/2022/07/FUqHEVVUsAAbZB0-1024x580.jpg", width=200)
    st.header("Data Science Recoded Batch")
    st.write("Pre recorded classes")
    if st.button("Enroll Recorded Class"):
        st.success("Enroll successfull to pre recorded class")

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "WhatsApp", "Mobile phone")
)

if add_selectbox:
    st.success(f"You've selected contact as: **{add_selectbox}**")

st.subheader("Expand to see all the topics we covered")
with st.expander("Topics we will cover: "):
    st.write("""
             1. Python basic to advance
             2. Statistics & Probability
             3. Numpy & Pandas
             4. Data visualization: Seaborn & Matplotlib
             5. ML Theory
             6. EDA & Feature Engineering
             7. Deep Learning
             8. End to end Data Science / ML projects 
""")
    
st.markdown("# Headline markdown")
st.markdown("> Blockquote markdown")