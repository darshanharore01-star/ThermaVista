import streamlit as st
import folium
from streamlit_folium import st_folium

from src.cities import CITIES
from src.landsat import get_landsat_image


def show():

    st.title("🛰 Satellite Viewer")

    # City selection
    city = st.selectbox(
        "Select City",
        list(CITIES.keys())
    )

    lat, lon = CITIES[city]

    # Year selection
    year = st.selectbox(
        "Select Year",
        [2022, 2023, 2024, 2025]
    )

    # Layer selection
    layer = st.radio(
        "Select Layer",
        [
            "True Color",
            "NDVI",
            "Land Surface Temperature"
        ]
    )

    # Create base map
    m = folium.Map(
        location=[lat, lon],
        zoom_start=11
    )

    try:
        # Get satellite tile from Earth Engine
        tile_url = get_landsat_image(lat, lon, year, layer)

        # Add satellite layer
        folium.TileLayer(
            tiles=tile_url,
            attr="Google Earth Engine",
            name=layer,
            overlay=True,
            control=True
        ).add_to(m)

        st.success(f"✅ {layer} layer loaded successfully!")

    except Exception as e:
        st.error(f"Error loading satellite image: {e}")

    # Add marker
    folium.Marker(
        [lat, lon],
        tooltip=city
    ).add_to(m)

    # Render map
    st_folium(
        m,
        width=900,
        height=600
    )