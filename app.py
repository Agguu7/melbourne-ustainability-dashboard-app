import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Melbourne Sustainability Dashboard",
    page_icon="🌿",
    layout="wide"
)

# Header
st.title("🌿 Melbourne Sustainability Dashboard")
st.subheader("Tracking Melbourne's future, powered by AI")

st.write("""
Welcome! This dashboard shows real sustainability data across 
Melbourne — pedestrian traffic, energy usage, and weather impact 
— with AI-powered predictions.
""")

# Three columns for key stats
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="🚶 Pedestrian Traffic", value="12,450", delta="+5% today")

with col2:
    st.metric(label="⚡ Energy Usage", value="8,230 kWh", delta="-3% today")

with col3:
    st.metric(label="🌡️ Temperature", value="24°C", delta="+2°C today")

st.divider()

st.info("📡 Data sourced from City of Melbourne Open Data Portal")