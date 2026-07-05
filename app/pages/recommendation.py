import streamlit as st

from src.cities import CITIES
from src.ai_heat import get_city_heat
from src.recommendation import recommend


def show():

    st.title("🌳 AI Cooling Recommendations")

    city = st.selectbox(
        "Select City",
        list(CITIES.keys())
    )

    year = st.selectbox(
        "Select Year",
        [2022, 2023, 2024, 2025],
        index=2
    )

    if st.button("Generate Recommendations"):

        try:

            result = get_city_heat(city, year)

            score = result["score"]

            st.metric(
                "Heat Score",
                f"{score:.2f}"
            )

            st.write(f"🌿 NDVI: {result['ndvi']:.3f}")
            st.write(f"🌡 LST: {result['lst']:.2f} K")
            st.write(f"⚠️ Risk: {result['risk']}")

            st.subheader("💡 Recommendations")

            for item in recommend(score):
                st.success(item)

        except Exception as e:
            st.error(e)