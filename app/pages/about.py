import streamlit as st


def show():

    st.title("ℹ️ About ThermaVista")

    st.markdown("""
## 🌍 ThermaVista

ThermaVista is an AI-powered Urban Heat Island (UHI) detection and cooling recommendation system that combines satellite imagery, Google Earth Engine, and Machine Learning to identify heat hotspots in urban areas.

The platform helps users visualize heat distribution, analyze vegetation, predict heat risk, and receive AI-driven recommendations for creating cooler and more sustainable cities.
""")

    st.markdown("---")

    st.header("🎯 Project Objectives")

    st.markdown("""
- 🛰 Analyze satellite imagery using Google Earth Engine
- 🌿 Calculate vegetation using NDVI
- 🌡 Analyze Land Surface Temperature (LST)
- 🤖 Predict urban heat risk using Machine Learning
- 📊 Visualize heat distribution with interactive dashboards
- 🌳 Recommend cooling strategies using AI
""")

    st.markdown("---")

    st.header("🛠 Technology Stack")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
### Backend
- Python
- Google Earth Engine
- Scikit-learn
- Pandas
- NumPy
""")

    with col2:
        st.markdown("""
### Frontend
- Streamlit
- Folium
- Plotly
- Streamlit-Folium
""")

    st.markdown("---")

    st.header("⚙️ System Workflow")

    st.markdown("""
1. 🛰 Fetch satellite imagery from Google Earth Engine
2. 🌿 Extract NDVI and Land Surface Temperature
3. 🤖 Process features using the ML model
4. 📈 Predict Heat Score
5. 🔥 Display Heat Risk Dashboard and Heat Map
6. 🌳 Generate AI-based cooling recommendations
""")

    st.markdown("---")

    st.header("🚀 Key Features")

    st.markdown("""
- 🛰 Satellite Viewer
- 🌿 NDVI Visualization
- 🌡 Land Surface Temperature Analysis
- 📊 Interactive Dashboard
- 🔥 AI Heat Map
- 🤖 Heat Prediction
- 🌳 Smart Cooling Recommendations
""")

    st.markdown("---")

    st.header("🔮 Future Scope")

    st.markdown("""
- Real-time satellite monitoring
- Multi-city comparison
- Climate change forecasting
- Mobile application
- IoT sensor integration
- AI-powered urban planning assistant
""")

    st.markdown("---")

    st.success("🌱 Building Cooler Cities with AI & Satellite Intelligence")