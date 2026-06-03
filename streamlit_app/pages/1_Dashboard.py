import streamlit as st
import pandas as pd
from theme import load_theme

st.set_page_config(layout="wide")

load_theme()

if not st.session_state.get("logged_in", False):
    st.switch_page("pages/0_Login.py")
    st.stop()

st.title("📈 Executive Dashboard")

# Load dataset
df = st.session_state.get("data")

if df is None:
    st.error("No dataset loaded.")
    st.stop()

# -------------------------------
# KPI CALCULATIONS
# -------------------------------

# Total Customers
total_customers = len(df)

# Churn Rate

churn_rate = 0

if "churn" in df.columns:

    churn_series = pd.to_numeric(
        df["churn"],
        errors="coerce"
    )

    churn_rate = round(
        churn_series.mean() * 100,
        2
    )

elif "Churned" in df.columns:

    if df["Churned"].dtype == "object":

        churn_rate = round(
            df["Churned"]
            .astype(str)
            .str.lower()
            .isin(
                [
                    "yes",
                    "true",
                    "1",
                    "churned"
                ]
            )
            .mean()
            * 100,
            2
        )

    else:

        churn_rate = round(
            pd.to_numeric(
                df["Churned"],
                errors="coerce"
            ).mean()
            * 100,
            2
        )
# Revenue
monthly_revenue = 0

if "monthly_fee" in df.columns:
    monthly_revenue = round(df["monthly_fee"].sum(), 2)

elif "Lifetime_Value" in df.columns:
    monthly_revenue = round(df["Lifetime_Value"].sum(), 2)

# Health Score
health_score = 0

if (
    "avg_weekly_usage_hours" in df.columns
    and "payment_failures" in df.columns
):

    health_score = round(
        (
            df["avg_weekly_usage_hours"].mean() * 5
        )
        -
        (
            df["payment_failures"].mean() * 10
        ),
        2
    )

elif (
    "Login_Frequency" in df.columns
    and "Email_Open_Rate" in df.columns
):

    health_score = round(
        (
            df["Login_Frequency"].mean()
            +
            df["Email_Open_Rate"].mean()
        ) / 2,
        2
    )
# -------------------------------
# KPI CARDS
# -------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        total_customers
    )

with col2:
    st.metric(
        "Churn Rate",
        f"{churn_rate}%"
    )

with col3:
    st.metric(
        "Revenue",
        f"₹{monthly_revenue:,.0f}"
    )

with col4:
    st.metric(
        "Health Score",
        health_score
    )

st.divider()

# -------------------------------
# DATASET PREVIEW
# -------------------------------

st.subheader("Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)

st.divider()

# -------------------------------
# BUSINESS SUMMARY
# -------------------------------

st.subheader("Business Summary")

st.success(f"""
Dataset contains {total_customers} records.

Current churn rate is {churn_rate}%.

Estimated revenue is ₹{monthly_revenue:,.0f}.

Average customer health score is {health_score}.
""")