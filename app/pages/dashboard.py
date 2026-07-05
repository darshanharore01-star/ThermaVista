import streamlit as st
import pandas as pd
import plotly.express as px

from src.cities import CITIES
from src.ai_heat import get_city_heat


def show():

    st.title("📊 Heat Risk Dashboard")

    data = []

    # Fetch AI prediction for each city
    for city in CITIES.keys():

        try:
            result = get_city_heat(city, 2024)

            data.append({
                "City": city,
                "Heat Score": round(result["score"], 2),
                "Risk": result["risk"],
                "NDVI": round(result["ndvi"], 3),
                "LST (K)": round(result["lst"], 2)
            })

        except Exception as e:
            st.warning(f"Could not load data for {city}: {e}")

    if len(data) == 0:
        st.error("No data available.")
        return

    df = pd.DataFrame(data)

    # Sort by Heat Score
    df = df.sort_values(
        by="Heat Score",
        ascending=False
    )

    # ===========================
    # Top Metrics
    # ===========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🏙 Cities Monitored",
            len(df)
        )

    with col2:
        st.metric(
            "📊 Average Heat Score",
            round(df["Heat Score"].mean(), 2)
        )

    with col3:
        st.metric(
            "🔥 Highest Heat Score",
            round(df["Heat Score"].max(), 2)
        )

    st.divider()

    # ===========================
    # Risk Summary
    # ===========================

    high = len(df[df["Risk"].str.contains("High")])
    medium = len(df[df["Risk"].str.contains("Medium")])
    low = len(df[df["Risk"].str.contains("Low")])

    c1, c2, c3 = st.columns(3)

    with c1:
        st.error(f"🔴 High Risk Cities: {high}")

    with c2:
        st.warning(f"🟡 Medium Risk Cities: {medium}")

    with c3:
        st.success(f"🟢 Low Risk Cities: {low}")

    st.divider()

    # ===========================
    # Hottest City
    # ===========================

    hottest = df.iloc[0]

    st.info(
        f"🔥 Hottest City: **{hottest['City']}** "
        f"with a Heat Score of **{hottest['Heat Score']}**"
    )

    st.divider()

    # ===========================
    # Data Table
    # ===========================

    st.subheader("📋 Heat Risk Table")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # ===========================
    # Bar Chart
    # ===========================

    st.subheader("📊 Heat Score Comparison")

    bar = px.bar(
        df,
        x="City",
        y="Heat Score",
        color="Heat Score",
        text="Heat Score",
        title="AI Predicted Heat Score by City"
    )

    st.plotly_chart(
        bar,
        use_container_width=True
    )

    st.divider()

    # ===========================
    # Line Chart
    # ===========================

    st.subheader("📈 Heat Score Trend")

    line = px.line(
        df,
        x="City",
        y="Heat Score",
        markers=True,
        title="Heat Score Trend Across Cities"
    )

    st.plotly_chart(
        line,
        use_container_width=True
    )

    st.divider()

    # ===========================
    # Pie Chart
    # ===========================

    st.subheader("🔥 Risk Distribution")

    pie = px.pie(
        df,
        names="Risk",
        title="Heat Risk Distribution"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

    st.divider()

    # ===========================
    # Download CSV
    # ===========================

    csv = df.to_csv(index=False)

    st.download_button(
        label="📥 Download Dashboard Report",
        data=csv,
        file_name="ThermaVista_Report.csv",
        mime="text/csv"
    )