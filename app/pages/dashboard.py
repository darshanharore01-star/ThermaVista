import streamlit as st

from src.cities import CITIES
from src.heat_score import calculate_heat_score


def show():
    st.success("Dashboard page loaded successfully!")
    st.title("📊 Heat Risk Dashboard")

    city = st.selectbox(
        "Select City",
        list(CITIES.keys())
    )

    score, risk = calculate_heat_score(city)

    st.metric(
        "Heat Score",
        score
    )

    st.metric(
        "Risk Level",
        risk
    )

    st.progress(score / 100)