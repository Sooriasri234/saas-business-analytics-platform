import streamlit as st
import pandas as pd
from theme import load_theme

st.set_page_config(layout="wide")

load_theme()

st.title(" AI Business Recommendations")

if not st.session_state.get("logged_in", False):
    st.switch_page("pages/0_Login.py")
    st.stop()

df = st.session_state.get("data")

if df is None:
    st.error("No dataset loaded.")
    st.stop()

st.subheader("Business Intelligence Recommendations")

# --------------------------
# CHURN ANALYSIS
# --------------------------

churn_rate = 0

if "Churned" in df.columns:

    if df["Churned"].dtype == "object":

        churn_rate = round(
            df["Churned"]
            .astype(str)
            .str.lower()
            .isin([
                "yes",
                "true",
                "1",
                "churned"
            ])
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

elif "churn" in df.columns:

    churn_rate = round(
        pd.to_numeric(
            df["churn"],
            errors="coerce"
        ).mean()
        * 100,
        2
    )
# --------------------------
# RECOMMENDATIONS
# --------------------------

if churn_rate > 40:

    st.error("⚠️ High Churn Risk Detected")

    st.markdown("""
### Recommended Actions

1. Launch retention campaigns

2. Offer loyalty rewards

3. Provide personalized discounts

4. Re-engage inactive users

5. Improve customer support
""")

else:

    st.success("✅ Customer Retention Healthy")

    st.markdown("""
### Growth Recommendations

1. Focus on new customer acquisition

2. Upsell premium subscriptions

3. Expand marketing campaigns

4. Increase referral incentives

5. Launch new premium features
""")

# --------------------------
# REVENUE ANALYSIS
# --------------------------

if "Lifetime_Value" in df.columns:

    revenue = round(
        df["Lifetime_Value"].sum(),
        2
    )

    st.metric(
        "Estimated Revenue",
        f"₹{revenue:,.0f}"
    )

    if revenue > 1000000:

        st.success(
            "Strong revenue performance detected."
        )

    else:

        st.warning(
            "Revenue growth opportunities available."
        )