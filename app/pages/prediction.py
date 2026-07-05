import streamlit as st

from src.recommendation import recommend
from src.cities import CITIES
from src.features import get_features
from src.predictor import predict_heat_score


def show():

    st.title("🤖 AI Heat Prediction")

    st.write(
        "Predict the Urban Heat Score using Google Earth Engine and Machine Learning."
    )

    # Select City
    city = st.selectbox(
        "Select City",
        list(CITIES.keys())
    )

    # Select Year
    year = st.selectbox(
        "Select Year",
        [2022, 2023, 2024, 2025]
    )

    lat, lon = CITIES[city]

    if st.button("Predict Heat Score"):

        with st.spinner("Fetching satellite data..."):

            try:
                # Get NDVI and LST from Earth Engine
                features = get_features(lat, lon, year)

                ndvi = features["ndvi"]
                lst = features["lst"]

                # Predict Heat Score
                score = predict_heat_score(ndvi, lst)

                st.success("✅ Prediction Completed")

                st.metric(
                    "Predicted Heat Score",
                    f"{score:.2f}"
                )

                st.write(f"🌿 NDVI: {ndvi:.3f}")
                st.write(f"🌡 Land Surface Temperature: {lst:.2f} K")

                # Risk Level
                if score >= 75:
                    st.error("🔴 High Heat Risk")

                elif score >= 50:
                    st.warning("🟡 Medium Heat Risk")

                else:
                    st.success("🟢 Low Heat Risk")

                # Recommendations
                st.subheader("💡 Recommendations")

                recommendations = recommend(score)

                for item in recommendations:
                    st.write(item)

            except Exception as e:
                st.error(f"Error: {e}")