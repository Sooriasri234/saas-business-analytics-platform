import streamlit as st
import pandas as pd
import plotly.express as px
from navbar import show_navbar
from theme import load_theme

st.set_page_config(layout="wide")

load_theme()
show_navbar()

if not st.session_state.get("logged_in", False):
    st.switch_page("pages/0_Login.py")
    st.stop()

st.title("Business Insights")

# Get dataset
df = st.session_state.get("data")

if df is None:
    st.error("No dataset loaded.")
    st.stop()

st.subheader("Dataset Overview")

st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

st.dataframe(df.head())

# Numerical Columns
numeric_cols = df.select_dtypes(include="number").columns

if len(numeric_cols) > 0:

    selected_col = st.selectbox(
        "Select Column for Analysis",
        numeric_cols
    )

    fig = px.histogram(
        df,
        x=selected_col,
        title=f"{selected_col} Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    fig2 = px.box(
        df,
        y=selected_col,
        title=f"{selected_col} Box Plot"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

else:
    st.warning(
        "No numerical columns found."
    )