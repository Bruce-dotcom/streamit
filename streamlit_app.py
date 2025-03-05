import streamlit as st

# Title
st.title("Mood Based App")


# Display message
mood = st.slider ("How Happy are you? (0=sad, 10+very Happy)",0,10,5)
energy= st.slider ("How Energitic do you fell? (0=Tired, 10=Full of Energy)",0,10,5)

if st.button("Get activity recommendation"):
    if mood >=7 and energy >=7:
        recommendation = "Go for a run or gym"
    elif mood >=7 and energy = 7:
        recommendation = "Watch a comedy movie or listen to music"
    elif mood < 7 and energy >= 7:
        recommendation = "Try meditation"
    else:
        recommendation = "Get your hands dirty with program"
    st.success(f"Recommended activity: {recommendation}")
