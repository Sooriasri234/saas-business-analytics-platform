import streamlit as st
import joblib
import numpy as np
from navbar import show_navbar
from theme import load_theme

st.set_page_config(layout="wide")

load_theme()
show_navbar()

st.title("Churn Prediction")
st.info(
    "Enter customer details below to predict the likelihood of churn."
)

if not st.session_state.get("logged_in", False):
    st.switch_page("pages/0_Login.py")
    st.stop()

# Load trained model
model = joblib.load("models/churn_model.pkl")

# Input Fields
plan_type = st.selectbox(
    "Plan Type",
    ["Basic", "Premium", "Standard"]
)

monthly_fee = st.number_input(
    "Monthly Fee",
    min_value=0,
    value=199
)

usage_hours = st.number_input(
    "Average Weekly Usage Hours",
    min_value=0.0,
    value=10.0
)

support_tickets = st.number_input(
    "Support Tickets",
    min_value=0,
    value=1
)

payment_failures = st.number_input(
    "Payment Failures",
    min_value=0,
    value=0
)

tenure_months = st.number_input(
    "Tenure Months",
    min_value=0,
    value=12
)

last_login_days = st.number_input(
    "Last Login Days Ago",
    min_value=0,
    value=5
)

st.markdown("---")

if st.button(
    "Predict Churn",
    use_container_width=True
):
    # Encoding used during training
    plan_mapping = {
        "Basic": 0,
        "Premium": 1,
        "Standard": 2
    }

    plan_encoded = plan_mapping[plan_type]

    features = np.array([[
        plan_encoded,
        monthly_fee,
        usage_hours,
        support_tickets,
        payment_failures,
        tenure_months,
        last_login_days
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0]

    churn_probability = probability[1] * 100

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Customer Likely to Churn")
    else:
        st.success("Customer Likely to Stay")

    st.metric(
        "Churn Probability",
        f"{churn_probability:.2f}%"
    )

    st.progress(int(churn_probability))

    # Optional Debug Section
    with st.expander("Show Input Details"):
        st.write({
            "Plan Type": plan_type,
            "Plan Encoded": plan_encoded,
            "Monthly Fee": monthly_fee,
            "Usage Hours": usage_hours,
            "Support Tickets": support_tickets,
            "Payment Failures": payment_failures,
            "Tenure Months": tenure_months,
            "Last Login Days": last_login_days
        })

st.markdown("---")
st.subheader("Dataset Churn Analysis")

df = st.session_state.get("data")

if df is not None:

    if "Churned" in df.columns:

        churn_rate = round(
            df["Churned"].mean() * 100,
            2
        )

        st.metric(
            "Dataset Churn Rate",
            f"{churn_rate}%"
        )

        if churn_rate > 40:

            st.error("""
High churn detected.

Recommendation:
Offer retention campaigns,
discounts and loyalty programs.
""")

        else:

            st.success("""
Churn levels are acceptable.

Recommendation:
Focus on customer acquisition
and upselling.
""")
            