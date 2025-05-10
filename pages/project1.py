import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="wide")
st.markdown("""
    <style>
    body, .main, .block-container {
        background-color: white !important;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding-top: 0;
        gap: 0;
    }
    .centered img {
        max-width: 100vw;
        height: auto;
        margin: 0;
        padding: 0;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='centered'>", unsafe_allow_html=True)

image_paths = [
    "assets/project1_1.png",
    "assets/project1_2.png",
    "assets/project1_3.png",
    "assets/project1_4.png"
]

for path in image_paths:
    if os.path.exists(path):
        img = Image.open(path)
        st.image(img, use_column_width=True)

st.markdown("</div>", unsafe_allow_html=True)
