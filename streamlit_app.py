import streamlit as st

# Title
st.title("Simple Calculator")


# Display message
num1 = st.number_input("Enter the first number:",value=0.0)
num2 = st.number_input("Enter the second number:",value=0.0)

operation = st.selectbox("Select operation: ",["Addition","Multiplication","Division"])

