import streamlit as st

st.title("🔢 Simple Calculator")

num_1 = st.number_input("Enter number1: ", value=0)
num_2 = st.number_input("Enter number2: ", value=0)

operation = st.selectbox("Select Operator: ", ["Addition", "Subtraction", "Multiplication", "Division"])

if st.button("Calculate"):
    if operation == "Addition":
        result = num_1 + num_2
    elif operation == "Subtraction":
        result = num_1 - num_2
    elif operation == "Multiplication":
        result = num_1 * num_2
    elif operation == "Division":
        if num_2 != 0:
            result = num_1 / num_2
        else:
            st.error("Number cannot divide by zero(0)")
            result = None
if result is not None:
    st.success(f"Result is: {result}")