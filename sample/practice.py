import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="My Digital Footprint", page_icon="🎓", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills & Achievements", "Customize Profile", "Contact"])

# Home Section
if page == "Home":
    st.title("🎓 My Digital Footprint – Showcasing My Journey")

    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150, caption="Profile Picture")
    else:
        st.image("sample/person.jpg", width=150, caption="Default Profile")

    # Personal Details
    name = st.text_input("Full Name:", "Bruce ISHIMWE")
    location = st.text_input("Location:", "Musanze, Rwanda")
    university = st.text_input("University:", "INES-Ruhengeri")
    field_of_study = st.text_input("Field of Study:", "BSc Computer Science, Year 3")

    st.write(f"📍 {location}")
    st.write(f"🏛 {university}")
    st.write(f"📚 {field_of_study}")

    # Resume Download
    with open("sample/CV-BRUCE ISHIMWE.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button("📄 Download Resume", data=resume_bytes, file_name="CV-BRUCE ISHIMWE.pd", mime="application/pdf")

    # About Me
    st.subheader("About Me")
    about_me = st.text_area("Short introduction:", "I am a passionate technologist!")
    st.write(about_me)

# Projects Section
elif page == "Projects":
    st.title("💻 My Projects")
    st.subheader("1️⃣ A project from Year 1, Year 2, Year 3 (Individual, Group Assignments, and Any Others)")
    st.subheader("2️⃣ Your Current Dissertation/Final Year Project")

    project_title = st.text_input("✔️ Project Title:", "E.g., Student Attendance System using Face Recognition")
    project_type = st.selectbox("✔️ Project Type:", ["Individual", "Group", "Class Assignment", "Internship Project"])
    project_description = st.text_area("✔️ Brief Description:", "Explain the problem, solution, and technologies used")
    project_link = st.text_input("✔️ Link to Code (if available):", "GitHub repo or research documentation")

    if st.button("Save Project"):
        st.success("Project details saved successfully!")
        st.write(f"**Project Title:** {project_title}")
        st.write(f"**Project Type:** {project_type}")
        st.write(f"**Description:** {project_description}")
        if project_link:
            st.write(f"[🔗 Project Link]({project_link})")

# Skills & Achievements Section
elif page == "Skills & Achievements":
    st.title("⚡ Skills & Achievements")

    st.subheader("Programming Skills")
    skills = {"Python": 90, "JavaScript": 80, "Machine Learning": 70, "Web Development": 85}
    for skill, level in skills.items():
        st.write(f"{skill}: {level}%")
        st.progress(level)

    st.subheader("Certifications & Achievements")
    achievements = [
        "✔ Google Data Analytics Certification",
        "✔ Hackathon Finalist at XYZ University",
        "✔ AI Research & Development Participant"
    ]
    for achievement in achievements:
        st.write(achievement)

# Customize Profile
elif page == "Customize Profile":
    st.title("🎨 Customize Your Profile")
    st.text_input("Edit Name")
    st.text_area("Edit About Me")
    st.file_uploader("Upload New Profile Picture", type=["jpg", "png"])

# Contact Section
elif page == "Contact":
    st.title("📬 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            with st.spinner("Sending..."):
                time.sleep(2)
                st.success("✅ Message sent successfully!")

    st.write("📧 Email: ishimwebruce30@gmail.com")
    st.write("[📂 GitHub](https://github.com)")

st.sidebar.write("---")
st.sidebar.write("🔹 Made with ❤ in Streamlit using my Head 😁")
