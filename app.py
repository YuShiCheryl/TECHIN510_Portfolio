import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="centered")

st.title("👩‍💻 Yu Shi's Portfolio")
st.write("Welcome! I'm a Master's student in Technology Innovation with a background in Architecture.")

st.header("🛠️ Projects")
st.subheader("📡 Humidity Sensing IoT Device")
st.write("An IoT device that measures humidity and displays it using a stepper motor and OLED.")
st.markdown("[View GitHub Repo](https://github.com/yourproject)")

st.subheader("🐾 MeowMatch – Pet Food Recommender Web App")
st.write("A Streamlit-based app that matches cats with suitable food based on health and preferences.")
st.markdown("[View GitHub Repo](https://github.com/yourproject)")

st.header("📫 Contact")
st.write("Email: yushi@email.com")
st.write("LinkedIn: [linkedin.com/in/yushi](https://linkedin.com/in/yushi)")
