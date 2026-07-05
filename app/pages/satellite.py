import streamlit as st
import folium
from streamlit_folium import st_folium

from src.cities import CITIES
from src.landsat import get_landsat_image


def show():

    st.title("🛰 Satellite Data Explorer")

    st.write(
        "View Landsat satellite imagery, vegetation (NDVI), and Land Surface Temperature using Google Earth Engine."
    )

    # ----------------------------
    # City Selection
    # ----------------------------
    city = st.selectbox(
        "📍 Select City",
        list(CITIES.keys())
    )

    lat, lon = CITIES[city]

    # ----------------------------
    # Year Selection
    # ----------------------------
    year = st.selectbox(
        "📅 Select Year",
        [2022, 2023, 2024, 2025],
        index=2
    )

    # ----------------------------
    # Layer Selection
    # ----------------------------
    layer = st.radio(
        "🛰 Select Layer",
        [
            "True Color",
            "NDVI",
            "Land Surface Temperature"
        ]
    )

    st.caption(f"📡 Showing: **{layer}** | **{year}** | **{city}**")

    # ----------------------------
    # Create Base Map
    # ----------------------------
    m = folium.Map(
        location=[lat, lon],
        zoom_start=11
    )

    try:

        with st.spinner("Loading satellite imagery..."):

            # Get Earth Engine Image
            image, vis_params = get_landsat_image(
                lat,
                lon,
                year,
                layer
            )

            # Convert to Map Tiles
            map_id = image.getMapId(vis_params)

            folium.TileLayer(
                tiles=map_id["tile_fetcher"].url_format,
                attr="Google Earth Engine",
                overlay=True,
                control=True,
                name=layer
            ).add_to(m)

            folium.LayerControl().add_to(m)

        st.success(f"✅ {layer} layer loaded successfully!")

    except Exception as e:

        st.error(f"❌ Error loading satellite image:\n{e}")

    # ----------------------------
    # City Marker
    # ----------------------------
    folium.Marker(
        [lat, lon],
        tooltip=city
    ).add_to(m)

    # ----------------------------
    # Display Map
    # ----------------------------
    st_folium(
        m,
        width=900,
        height=600,
        returned_objects=[]
    )

    st.markdown("---")

    # ----------------------------
    # Selected Information
    # ----------------------------
    st.subheader("📋 Selected Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📍 City", city)

    with col2:
        st.metric("📅 Year", year)

    with col3:
        st.metric("🛰 Layer", layer)

    st.markdown("---")

    # ----------------------------
    # Layer Legend
    # ----------------------------
    st.subheader("🎨 Layer Legend")

    if layer == "True Color":
        st.info(
            """
🛰 **True Color**

Displays natural satellite imagery exactly as seen from space.
"""
        )

    elif layer == "NDVI":
        st.success(
            """
🌿 **NDVI (Normalized Difference Vegetation Index)**

🟤 Brown → Very Low Vegetation

🟡 Yellow → Sparse Vegetation

🟢 Green → Dense Healthy Vegetation
"""
        )

    elif layer == "Land Surface Temperature":
        st.warning(
            """
🌡 **Land Surface Temperature**

🔵 Blue → Cool Surface

🟢 Green → Moderate Temperature

🟠 Orange → Warm Surface

🔴 Red → Very Hot Surface
"""
        )

    st.markdown("---")

    st.info("🛰 Satellite Source: Google Earth Engine | Landsat 8 Collection")