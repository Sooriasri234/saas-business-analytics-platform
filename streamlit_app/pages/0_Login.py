import streamlit as st
from auth import google_login

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🔐 SaaS Analytics Platform")

st.markdown("### Welcome")

st.info(
    "Please login with your Google account to access the dashboard."
)

# If already logged in
if st.session_state.get("logged_in", False):

    st.success(
        f"✅ Logged in as {st.session_state.get('user_name', 'User')}"
    )

    st.write(
        f"📧 {st.session_state.get('user_email', '')}"
    )

    if st.button(
        "🚀 Go To Dashboard",
        use_container_width=True
    ):
        st.switch_page("app.py")

# Show Google Login Button
else:

    st.markdown("### Sign In")

    google_login()

    st.markdown("---")

    st.caption(
        "Secure login powered by Google OAuth 2.0"
    )