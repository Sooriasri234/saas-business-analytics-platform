import streamlit as st

st.title("💚 Customer Health Score")

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

last_login_days = st.number_input(
    "Last Login Days Ago",
    min_value=0,
    value=5
)

if st.button("Calculate Health Score"):

    score = 100

    score -= payment_failures * 5
    score -= support_tickets * 3
    score -= last_login_days * 0.5
    score += usage_hours

    score = max(0, min(100, score))

    st.subheader("Customer Health Result")

    st.metric(
        "Health Score",
        f"{score:.1f}/100"
    )

    st.progress(int(score))

    if score >= 80:
        st.success("🟢 Healthy Customer")

    elif score >= 60:
        st.warning("🟡 Moderate Risk Customer")

    else:
        st.error("🔴 High Risk Customer")