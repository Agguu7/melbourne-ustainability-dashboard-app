import streamlit as st
import pandas as pd
import plotly.express as px
from data import get_pedestrian_data

st.set_page_config(page_title="Melbourne Sustainability Dashboard", page_icon="🌿", layout="wide")

st.title("🌿 Melbourne Sustainability Dashboard")
st.subheader("Tracking Melbourne's future, powered by AI")

with st.spinner("Loading real Melbourne data..."):
    df = get_pedestrian_data()

col1, col2, col3 = st.columns(3)

with col1:
    total = df["pedestriancount"].sum()
    st.metric(label="🚶 Total Pedestrians", value=f"{total:,}")

with col2:
    avg = int(df["pedestriancount"].mean())
    st.metric(label="📊 Average Count", value=f"{avg:,}")

with col3:
    sensors = df["sensor_name"].nunique()
    st.metric(label="📡 Active Sensors", value=sensors)

st.divider()

st.subheader("📊 Pedestrian Traffic by Location")
fig1 = px.bar(
    df.groupby("sensor_name")["pedestriancount"].sum().reset_index(),
    x="sensor_name",
    y="pedestriancount",
    color="pedestriancount",
    color_continuous_scale="Greens",
    labels={"sensor_name": "Location", "pedestriancount": "Total Pedestrians"},
)
fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

st.subheader("📋 Latest Pedestrian Sensor Readings")
st.dataframe(df[["sensing_date", "sensor_name", "pedestriancount", "direction_1", "direction_2"]])

st.info("📡 Data sourced from City of Melbourne Open Data Portal")
