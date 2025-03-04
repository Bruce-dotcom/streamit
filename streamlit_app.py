import streamlit as st

# Title
st.title("Simple Calculator")


# Display message
num1 = st.number_input("Enter the first number:",value=0.0)
num2 = st.number_input("Enter the second number:",value=0.0)

operation = st.selectbox("Select operation: ",["Addition","Subtraction","Multiplication","Division"])

if st.button("Calculate"):
    if operation =="Addition":
        result = num1+num2
    elif operation == "Subtraction":
        result = num1-num2
    elif operation == "Multiplication":
        result = num1*num2
    elif operation == "Division":
        result = num1/num2
    st.success(f"Result:{result}")
