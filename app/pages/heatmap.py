import streamlit as st
import folium
from streamlit_folium import st_folium

from src.cities import CITIES
from src.ai_heat import get_city_heat


def show():

    st.title("🔥 AI Heat Risk Map")

    year = st.selectbox(
        "Select Year",
        [2022, 2023, 2024, 2025],
        index=2
    )

    m = folium.Map(
        location=[22.5, 79.0],
        zoom_start=5
    )

    for city, (lat, lon) in CITIES.items():

        try:

            result = get_city_heat(city, year)

            score = result["score"]
            risk = result["risk"]
            ndvi = result["ndvi"]
            lst = result["lst"]

            if score >= 75:
                color = "red"
            elif score >= 50:
                color = "orange"
            else:
                color = "green"

            popup = f"""
            <h4>{city}</h4>

            <b>🔥 Heat Score:</b> {score:.2f}<br>

            <b>⚠️ Risk:</b> {risk}<br>

            <b>🌿 NDVI:</b> {ndvi:.3f}<br>

            <b>🌡 LST:</b> {lst:.2f} K
            """

            folium.CircleMarker(
                location=[lat, lon],
                radius=10,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.8,
                popup=popup,
                tooltip=city
            ).add_to(m)

        except Exception as e:

            folium.Marker(
                location=[lat, lon],
                tooltip=f"{city} (Error)",
                popup=str(e)
            ).add_to(m)

    folium.LayerControl().add_to(m)

    st_folium(
        m,
        width=1000,
        height=650,
        returned_objects=[]
    )