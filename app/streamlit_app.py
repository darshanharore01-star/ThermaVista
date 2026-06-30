import streamlit as st
from streamlit_option_menu import option_menu

# Import all pages
from pages import (
    home,
    dashboard,
    satellite,
    heatmap,
    prediction,
    recommendation,
    about,
)

st.set_page_config(
    page_title="ThermaVista",
    page_icon="🌍",
    layout="wide"
)

# Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="🌍 ThermaVista",
        options=[
            "Home",
            "Dashboard",
            "Satellite Data",
            "Heat Map",
            "AI Prediction",
            "Recommendations",
            "About"
        ],
        icons=[
            "house",
            "bar-chart",
            "globe",
            "thermometer-half",
            "cpu",
            "tree",
            "info-circle"
        ],
        default_index=0,
    )

# Page Routing
if selected == "Home":
    home.show()

elif selected == "Dashboard":
    dashboard.show()

elif selected == "Satellite Data":
    satellite.show()

elif selected == "Heat Map":
    heatmap.show()

elif selected == "AI Prediction":
    prediction.show()

elif selected == "Recommendations":
    recommendation.show()

elif selected == "About":
    about.show()