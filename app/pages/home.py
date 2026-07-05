import streamlit as st


def show():

    st.title("🌍 ThermaVista")

    st.subheader("AI-Powered Urban Heat Island Detection & Cooling Recommendation System")

    st.info("🌍 Welcome to ThermaVista")

    st.markdown("---")

    st.markdown("""
ThermaVista is an AI-powered platform that helps identify **Urban Heat Islands (UHI)** using satellite imagery and machine learning.

The system analyzes satellite data to detect heat hotspots, estimate heat risk, and provide recommendations to improve urban sustainability.
""")

    st.markdown("---")

    st.header("🚀 Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
### 🛰 Satellite Analysis

- True Color Imagery
- NDVI Analysis
- Land Surface Temperature
- Google Earth Engine
""")

    with col2:
        st.markdown("""
### 🤖 Artificial Intelligence

- Heat Risk Prediction
- Machine Learning
- Smart Recommendations
- Interactive Dashboard
""")

    st.markdown("---")

    st.header("📊 Project Statistics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Cities",
        "7"
    )

    c2.metric(
        "Satellite",
        "Landsat 8"
    )

    c3.metric(
        "AI Model",
        "Random Forest"
    )

    c4.metric(
        "Prediction",
        "Real-Time"
    )

    st.markdown("---")

    st.header("🛠 Technology Stack")

    st.markdown("""
- 🐍 Python
- 🌐 Streamlit
- 🛰 Google Earth Engine
- 🤖 Scikit-learn
- 🗺 Folium
- 📊 Plotly
- 🐼 Pandas
""")

    st.markdown("---")

    st.success(
        "🌱 Building smarter and cooler cities using AI and Satellite Data."
    )