import streamlit as st

#Set the Page Title
st.set_page_config(page_title="Student Portfolio", page_icon="🎓",layout="wide")

#side navigation
st.sidebar.title("📌 Navigation")
page = st.siderbar.radio("Go to", ["Home","Projects","skills","customize profile","Contact"])

#Home section
if page == "Home":
    st.title (" Student Portfolio")

    #Profile picture upload
    uploaded_image = st.file_uploader("Upload profile picture", type["jpg","png"])
    if uploaded_image:
        st.image(uploaded_image, width=150,caption="Profile Picture")
    else:
        st.image("person.jpg", width=150,caption="Default Profile Picture")
#student details
name = st.text_input("Your Name","ISHIMWE Bruce")
location = st.text_input("Location", "Musanze,Rwanda")
field_of_study = st.text_input("Field of study", "Computer Science")
university = st.text_input("university","INES-Ruhengeri")

st.write(f"📍 {location}")
st.write(f"📚 {field_of_study}")
st.write(f"🏫 {university}")