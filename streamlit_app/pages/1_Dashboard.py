import streamlit as st
from theme import load_theme

st.set_page_config(layout="wide")

load_theme()

st.title("📈 Executive Dashboard")

if not st.session_state.get("logged_in", False):
    st.switch_page("pages/0_Login.py")
    st.stop()
    

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", "2800")

with col2:
    st.metric("Churn Rate", "57.32%")

with col3:
    st.metric("Monthly Revenue", "₹12.16 Lakh")

with col4:
    st.metric("Avg Health Score", "73.48")

st.markdown("---")

st.subheader("Business Summary")

st.success("""
The SaaS platform currently has 2800 customers generating
₹12.16 lakh monthly revenue.

The churn rate is 57.32%, indicating customer retention
needs improvement.

Average customer health score is 73.48, placing most
customers in the Moderate Risk category.
""")