import streamlit as st
from PIL import Image
import base64
import os
from io import BytesIO

# ------------------------
# Streamlit Page Setup
# ------------------------
st.set_page_config(layout="wide")

# ------------------------
# Custom CSS for Hover Effect (fixed square images)
# ------------------------
st.markdown("""
    <style>
    .project-card {
        position: relative;
        overflow: hidden;
        transition: transform 0.3s ease-in-out;
        margin-bottom: 20px;
    }
    .project-card:hover {
        transform: scale(1.05);
        z-index: 2;
    }
    .project-image {
        width: 100%;
        aspect-ratio: 1 / 1;
        object-fit: cover;
        display: block;
    }
    .overlay-text {
        position: absolute;
        bottom: 0;
        background: rgba(0,0,0,0.6);
        color: white;
        width: 100%;
        text-align: center;
        padding: 8px 0;
        font-size: 16px;
        opacity: 0;
        transition: opacity 0.3s ease-in-out;
    }
    .project-card:hover .overlay-text {
        opacity: 1;
    }
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 10px 30px 30px 30px;
        font-family: sans-serif;
    }
    .portfolio-title {
        font-size: 20px;
        letter-spacing: 2px;
    }
    .portfolio-email {
        font-size: 14px;
        color: #555;
    }
    a { text-decoration: none; color: inherit; }
    </style>
""", unsafe_allow_html=True)

# ------------------------
# Header Bar
# ------------------------
st.markdown("""
    <div class="top-bar">
        <div class="portfolio-title">Yu Shi Portfolio</div>
        <div class="portfolio-email">cherylshiy@gmail.com</div>
    </div>
""", unsafe_allow_html=True)

# ------------------------
# Image Processing Function
# ------------------------
def crop_square(image, size=(600, 600)):
    width, height = image.size
    min_dim = min(width, height)
    left = (width - min_dim) // 2
    top = (height - min_dim) // 2
    image = image.crop((left, top, left + min_dim, top + min_dim))
    return image.resize(size)

def image_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

# ------------------------
# Project Data
# ------------------------
projects = [
    {"path": "assets/1.png", "title": "Aurelian Wall Intervention", "term": "Fall 2021", "link": "project1"},
    {"path": "assets/2.png", "title": "Slum Renovation", "term": "Spring 2021", "link": "project2"},
    {"path": "assets/3.png", "title": "Catalog Homes", "term": "Fall 2020", "link": "project3"},
    {"path": "assets/4.png", "title": "Tension Structure", "term": "Spring 2022", "link": "project4"},
    {"path": "assets/5.png", "title": "Site Cloister", "term": "Fall 2019", "link": "project5"},
    {"path": "assets/6.png", "title": "Hand Drawings & Model Making", "term": "", "link": "project6"},
]

# ------------------------
# Layout and Rendering
# ------------------------
cols = st.columns(3)
for i, project in enumerate(projects):
    col = cols[i % 3]
    with col:
        if os.path.exists(project["path"]):
            img = Image.open(project["path"])
            img_square = crop_square(img)
            img_b64 = image_to_base64(img_square)

            image_tag = f"<img class='project-image' src='data:image/png;base64,{img_b64}' />"
            overlay = f"<div class='overlay-text'><div style='font-weight:bold'>{project['title']}</div><div style='font-size:14px'>{project['term']}</div></div>"
            content = f"<div class='project-card'>{image_tag}{overlay}</div>"

            if project["link"]:
                content = f"<a href='/{project['link']}' target='_self'>{content}</a>"

            st.markdown(content, unsafe_allow_html=True)
