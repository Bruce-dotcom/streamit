import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Digital Footprint", page_icon="🎓", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Customize Profile", "Contact"])

# Home Section
if page == "Home":
    st.title("🎓 My Digital Footprint – Showcasing My Journey")

    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150, caption="Profile Picture")
    else:
        st.image("default_profile.jpg", width=150, caption="Default Profile")

    # Personal Details
    name = st.text_input("Full Name:", "Your Name")
    location = st.text_input("Location:", "City, Country")
    university = st.text_input("University:", "Your University")
    field_of_study = st.text_input("Field of Study:", "Your Field")

    st.write(f"📍 {location}")
    st.write(f"🏛 {university}")
    st.write(f"📚 {field_of_study}")

    # Resume Download
    with open("resume.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button("📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")

    # About Me
    st.subheader("About Me")
    about_me = st.text_area("Short introduction:", "I am a passionate technologist!")
    st.write(about_me)

# Projects Section
elif page == "Projects":
    st.title("💻 My Projects")
    category = st.selectbox("Filter by:", ["All", "Year 1", "Year 2", "Final Year", "Group Project"])

    with st.expander("📊 Data Analysis Project"):
        st.write("Analyzed Rwanda GDP trends using Pandas & Matplotlib.")
        st.write("[🔗 GitHub](https://github.com)")

    with st.expander("🤖 AI Chatbot"):
        st.write("Developed an AI chatbot using Python & NLP.")
        st.write("[🔗 GitHub](https://github.com)")

# Skills Section
elif page == "Skills":
    st.title("⚡ Skills & Achievements")

    st.subheader("Programming Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)
    skill_js = st.slider("JavaScript", 0, 100, 80)
    st.progress(skill_js)
    skill_ml = st.slider("Machine Learning", 0, 100, 70)
    st.progress(skill_ml)

    st.subheader("Certifications & Achievements")
    st.write("✔ Google Data Analytics Certification")
    st.write("✔ Hackathon Finalist at XYZ University")

# Customize Profile
elif page == "Customize Profile":
    st.title("🎨 Customize Your Profile")
    st.text_input("Edit Name")
    st.text_area("Edit About Me")

# Contact Section
elif page == "Contact":
    st.title("📬 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully!")

    st.write("📧 Email: your.email@example.com")
    st.write("[🔗 LinkedIn](https://linkedin.com)")
    st.write("[📂 GitHub](https://github.com)")

st.sidebar.write("---")
st.sidebar.write("🔹 Made with ❤ in Streamlit")
