import streamlit as st
import joblib
import numpy as np

st.title("🤖 Churn Prediction")

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

if st.button("Predict Churn"):

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
        st.error("⚠️ Customer Likely to Churn")
    else:
        st.success("✅ Customer Likely to Stay")

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