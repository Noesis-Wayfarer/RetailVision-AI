import streamlit as st
import pandas as pd

st.set_page_config(page_title="RetailVision AI", page_icon="🛒", layout="wide",initial_sidebar_state="collapsed")

st.title("🛒 RetailVision AI")

st.caption("Retail Intelligence Platform")

st.markdown("""
            Monitor : Customer Movement, Dwell Time and Shopping Behavior.
            """)

st.divider()

# Video Feed
st.subheader("🎥 AI Processed Video Feed")

left, center, right = st.columns([1, 8, 1])

with center:
    st.video("retail_analytics_output.mp4")

st.divider()

# KPI 
summary = pd.read_csv("summary.csv")
zone_df = pd.read_csv("zone_analytics.csv")

most_active_zone = zone_df.loc[
    zone_df["Visits"].idxmax(), "Zone"
]

st.subheader("📊 Key Performance Indicators")

cards = [
    ("👥", "Unique Customers", summary.iloc[0]["Value"], "Total Visitors Detected"),
    ("📈", "Peak Occupancy", summary.iloc[1]["Value"], "Maximum Simultaneous Customers"),
    ("🔥", "Most Active Zone", most_active_zone, "Highest Customer Activity"),
    ("🎯", "Tracking Records", summary.iloc[2]["Value"], "Tracking Points Analysed")
]

cols = st.columns(4)

for col, (icon, title, value, subtitle) in zip(cols, cards):
    with col:
        st.markdown(f"""
        <div style="
            background: linear-gradient(180deg,#1e293b,#0f172a);
            border:1px solid #334155;
            border-radius:18px;
            padding:22px;
            height:190px;
        ">

        <div style="
            font-size:32px;
            margin-bottom:12px;
        ">
            {icon}
        </div>

        <div style="
            color:#94a3b8;
            font-size:15px;
            font-weight:600;
        ">
            {title}
        </div>

        <div style="
            font-size:24px;
            font-weight:670;
            color:white;
            margin-top:8px;
            margin-bottom:12px;
        ">
            {value}
        </div>

        <div style="
            color:#64748b;
            font-size:13px;
        ">
            {subtitle}
        </div>

        </div>
        """, unsafe_allow_html=True)

st.divider()
# Heatmap

st.subheader("🔥 Customer Movement Heatmap")
left, center, right = st.columns([1, 6, 1])

with center:
    st.image("retail_heatmap_overlay.png", use_container_width=True)
st.caption("Warmer colors indicate higher customer activity.")

st.divider()

col1, col2 = st.columns(2)
with col1:
  st.subheader("📍 Zone Performance") # Zone Analytics
  zone_df = pd.read_csv("zone_analytics.csv")
  st.dataframe(zone_df, width="stretch", hide_index=True)

with col2:
  st.subheader("⏱ Customer Engagement Analysis") # Dwell Time Analysis
  dwell_df = pd.read_csv("dwell_time.csv")
  st.dataframe(dwell_df, width="stretch", hide_index=True)
st.divider()

# Footer
st.caption(
    "Built with using YOLOv8 • DeepSORT • OpenCV • Streamlit"
)