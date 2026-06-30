import streamlit as st
import plotly.express as px
import pandas as pd

def show():
    st.title("📊 Dashboard")

    st.subheader("Urban Heat Monitoring")

    # Metrics
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🔥 Hotspots", "245", "+12")
    c2.metric("🌡 Avg Temp", "39.2°C", "+0.8°C")
    c3.metric("🌳 Green Cover", "27%", "-2%")
    c4.metric("🏙 Risk Zones", "18", "+3")

    st.divider()

    # Sample Data
    df = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Temperature":[35,36,37,39,40,41,39]
    })

    fig = px.line(
        df,
        x="Day",
        y="Temperature",
        markers=True,
        title="Weekly Temperature Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("🗺 Heat Map")

    st.info("Heat Map will be displayed here in the next module.")