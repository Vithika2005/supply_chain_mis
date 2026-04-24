import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Supply Chain MIS", layout="wide")

st.title("📦 Intelligent IoT-Enabled Supply Chain MIS")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Inventory", "Sensors", "Alerts", "Forecast"])

# Fetch APIs
def get_data(endpoint):
    try:
        return requests.get(f"http://127.0.0.1:5000/{endpoint}").json()
    except:
        return {}

# ---------------- DASHBOARD ----------------
if page == "Dashboard":
    st.header("📊 Overview")

    sensor = get_data("sensor")
    inventory = get_data("inventory")

    col1, col2, col3 = st.columns(3)

    col1.metric("🌡 Temperature", f"{sensor.get('temperature', 0):.2f} °C")
    col2.metric("💧 Humidity", f"{sensor.get('humidity', 0):.2f} %")
    col3.metric("📦 Stock Level", sensor.get("stock_level", 0))

# ---------------- INVENTORY ----------------
elif page == "Inventory":
    st.header("📦 Inventory Management")

    inventory = get_data("inventory")

    df = pd.DataFrame(inventory)

    if not df.empty:
        st.dataframe(df)

        fig = px.bar(df, x="product", y="quantity", title="Stock Levels")
        st.plotly_chart(fig, use_container_width=True)

        low_stock = df[df["quantity"] < 30]
        st.subheader("⚠ Low Stock Items")
        st.write(low_stock if not low_stock.empty else "All good 👍")

    else:
        st.warning("No inventory data available")

# ---------------- SENSORS ----------------
elif page == "Sensors":
    st.header("🌡 Sensor Monitoring")

    sensor = get_data("sensor")

    st.json(sensor)

# ---------------- ALERTS ----------------
elif page == "Alerts":
    st.header("🚨 Alerts System")

    sensor = get_data("sensor")

    alerts = sensor.get("alerts", [])

    if alerts:
        for alert in alerts:
            st.error(alert)
    else:
        st.success("No alerts 🚀")

# ---------------- FORECAST ----------------
elif page == "Forecast":
    st.header("📈 Demand Forecast")

    forecast = get_data("forecast")

    st.json(forecast)
