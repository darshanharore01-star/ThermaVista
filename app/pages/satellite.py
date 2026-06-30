import streamlit as st
import ee
import folium
from streamlit_folium import st_folium

PROJECT_ID = "nth-mantra-501009-e8"

ee.Initialize(project=PROJECT_ID)


def show():

    st.title("🛰 Satellite Data")

    st.write("Real Landsat 8 imagery from Google Earth Engine")

    m = folium.Map(
        location=[18.5204, 73.8567],
        zoom_start=10
    )

    st_folium(
        m,
        width=900,
        height=600
    )