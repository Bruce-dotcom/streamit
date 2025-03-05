import streamlit as st

#Set the Page Title
st.set_page_config(page_title="Student Portfolio", page_icon="🎓",layout="wide")

#side navigation
st.siderbar.title("📌 Navigation")
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