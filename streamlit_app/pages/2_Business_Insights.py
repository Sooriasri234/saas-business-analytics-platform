import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Business_Insights")

st.markdown("""
Explore customer behavior, subscription trends,
and business performance insights.
""")

plan_data = pd.DataFrame({
    "Plan": ["Premium", "Standard", "Basic"],
    "Customers": [944, 933, 923]
})

fig = px.pie(
    plan_data,
    names="Plan",
    values="Customers",
    title="Plan Distribution"
)

st.plotly_chart(fig, use_container_width=True)

risk_data = pd.DataFrame({
    "Risk": ["Healthy", "Moderate Risk", "High Risk"],
    "Count": [995, 1256, 549]
})

fig2 = px.bar(
    risk_data,
    x="Risk",
    y="Count",
    title="Customer Risk Categories"
)

st.plotly_chart(fig2, use_container_width=True)