import streamlit as st

# Set the Page Title
st.set_page_config(page_title="Student Portfolio", page_icon="🎓", layout="wide")

# Side navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Customize Profile", "Contact"])

# Home section
if page == "Home":
    st.title("Student Portfolio")

    # Profile picture upload
    uploaded_image = st.file_uploader("Upload profile picture", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150, caption="Profile Picture")
    else:
        st.image("Portfolio/person.jpg", width=150, caption="Default Profile Picture")

    # Student details
    name = st.text_input("Your Name", "ISHIMWE Bruce")
    location = st.text_input("Location", "Musanze, Rwanda")
    field_of_study = st.text_input("Field of Study", "Computer Science")
    university = st.text_input("University", "INES-Ruhengeri")

    # Display details
    st.write(f"📍 {location}")
    st.write(f"📚 {field_of_study}")
    st.write(f"🏫 {university}")

#Download resume
with open("Portfolio/CV-BRUCE ISHIMWE.pdf","rb") as file:
    resume_bytes = file.read()
st.download_button(label="📄, Download Resume", data=resume_bytes, file_name="CV-BRUCE ISHIMWE.pdf",mime="application/pdf")

st.markdown("-------------")
st.subheader("About Me")
about_me == st.text_area("Write a short description about yourself:","I am a passionate AI Student")

st.write(about_me)

#Projects page
elif page== "Projects":
    st.title("💻 My Projects")

