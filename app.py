import streamlit as st

st.set_page_config(page_title="Decision Support System", layout="wide")

st.title("📊 Decision Support System v3.0")
st.markdown("---")

st.sidebar.header("🎛️ Control Panel")

# Recreating the Excel inputs as Streamlit Sliders
market_demand = st.sidebar.number_input("Market Demand Factor", value=85.0)
op_cost = st.sidebar.number_input("Operational Cost Index", value=112.5)
risk_tolerance = st.sidebar.slider("Risk Tolerance Level", min_value=1, max_value=10, value=3)
supply_chain = st.sidebar.number_input("Supply Chain Efficiency", value=94.0)

st.write("### Current System Inputs")
st.write(f"- **Market Demand:** {market_demand}")
st.write(f"- **Operational Cost:** {op_cost}")
st.write(f"- **Risk Tolerance:** {risk_tolerance}")
st.write(f"- **Supply Chain Efficiency:** {supply_chain}%")
