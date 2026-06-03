import streamlit as st
from navbar import show_navbar
from theme import load_theme

st.set_page_config(layout="wide")

load_theme()
show_navbar()

st.title("💚 Customer Health Score")
st.info(
    "Evaluate overall customer engagement and health using activity metrics."
)

if not st.session_state.get("logged_in", False):
    st.switch_page("pages/0_Login.py")
    st.stop()

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

st.markdown("---")

if st.button(
    "❤️ Calculate Health Score",
    use_container_width=True
):

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

# --st.markdown("---")
st.subheader("📊 Dataset Health Analysis")

df = st.session_state.get("data")

if df is not None:

    st.write("Dataset Loaded Successfully")

    if (
        "Login_Frequency" in df.columns
        and "Email_Open_Rate" in df.columns
    ):

        avg_health = round(
            (
                df["Login_Frequency"].mean()
                +
                df["Email_Open_Rate"].mean()
            ) / 2,
            2
        )

        st.metric(
            "Average Dataset Health Score",
            avg_health
        )

        if avg_health >= 70:
            st.success(
                "Dataset indicates healthy customers."
            )
        elif avg_health >= 50:
            st.warning(
                "Dataset indicates moderate-risk customers."
            )
        else:
            st.error(
                "Dataset indicates high-risk customers."
            )