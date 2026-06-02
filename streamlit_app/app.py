import streamlit as st

st.set_page_config(
    page_title="SaaS Business Analytics Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 SaaS Business Analytics & Prediction Platform")

st.markdown("""
Welcome to the SaaS Business Analytics Platform.

### Features

- Customer Analytics
- Revenue Analytics
- SQL Insights
- Churn Prediction
- Customer Health Score

Use the sidebar to navigate between pages.
""")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Customers", "2800")
col2.metric("Churn Rate", "57.32%")
col3.metric("Monthly Revenue", "₹12.16L")
col4.metric("Health Score", "73.48")