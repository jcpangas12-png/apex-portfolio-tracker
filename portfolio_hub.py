import streamlit as st
import pandas as pd
import numpy as np

# Set up a global luxury tech aesthetic (Dark Theme Baseline)
st.set_page_config(page_title="Apex Portfolio Tracker", page_icon="📈", layout="wide")

# Custom CSS injector to make it look like a $100 premium template
st.markdown("""
    <style>
    .main { background-color: #0f1115; color: #e4e6eb; }
    div.block-container { padding-top: 2rem; }
    .stButton>button { background-color: #1f232b; color: #00ff66; border: 1px solid #303642; }
    .stButton>button:hover { background-color: #00ff66; color: #0f1115; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 Apex Portfolio Analytics Dashboard")
st.write("Welcome to your premium investment asset control panel. Track holdings and calculate global returns.")

# 1. Sidebar Control Panel for Global Entries
st.sidebar.header("🛡️ Assets Control Panel")
asset_name = st.sidebar.text_input("Asset Ticker / Name (e.g., BTC, AAPL)", value="BTC")
qty = st.sidebar.number_input("Total Units Held", min_value=0.0, value=1.5, step=0.1)
buy_price = st.sidebar.number_input("Average Buy Price ($)", min_value=0.0, value=62000.0, step=100.0)
current_price = st.sidebar.number_input("Current Market Price ($)", min_value=0.0, value=65200.0, step=100.0)

# 2. Portfolio Mathematics (Pure Python Logic)
total_cost = qty * buy_price
current_value = qty * current_price
net_profit_loss = current_value - total_cost
roi_percentage = (net_profit_loss / total_cost) * 100 if total_cost > 0 else 0.0

# 3. High-End Premium Key Metric Blocks Layout
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Total Capital Invested", value=f"${total_cost:,.2f}")
with col2:
    st.metric(label="Current Portfolio Value", value=f"${current_value:,.2f}")
with col3:
    st.metric(label="Net Profit / Loss", value=f"${net_profit_loss:,.2f}", delta=f"${net_profit_loss:,.2f}")
with col4:
    st.metric(label="Total Return (ROI)", value=f"{roi_percentage:.2f}%", delta=f"{roi_percentage:.2f}%")

st.markdown("---")

# 4. Interactive Simulation Charting
st.subheader("📊 Growth Trajectory Visualizer")
st.write("Simulated standard performance variance over a 30-day tracking window:")

# Generate realistic mock volatility data for the chart layout
chart_days = 30
np.random.seed(42)
price_swings = np.random.normal(0.002, 0.02, chart_days)
price_path = current_value * (1 + price_swings).cumsum()

chart_data = pd.DataFrame({
    'Days Tracking': range(1, chart_days + 1),
    'Portfolio Value Valuation ($)': price_path
}).set_index('Days Tracking')

st.line_chart(chart_data)

# 5. Asset Ledger Logs Table
st.subheader("📋 Core Holdings Ledger Logs")
ledger_df = pd.DataFrame([
    {"Asset": asset_name, "Holdings": qty, "Avg Buy Price": f"${buy_price:,.2f}", "Current Price": f"${current_price:,.2f}", "Current Valuation": f"${current_value:,.2f}"},
    {"Asset": "ETH", "Holdings": 12.0, "Avg Buy Price": "$2,400.00", "Current Price": "$2,650.00", "Current Valuation": "$31,800.00"},
    {"Asset": "SOL", "Holdings": 45.0, "Avg Buy Price": "$135.00", "Current Price": "$152.00", "Current Valuation": "$6,840.00"}
])
st.table(ledger_df)
