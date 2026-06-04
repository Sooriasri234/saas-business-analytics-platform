import streamlit as st
from auth import google_login
from theme import load_theme

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# -----------------------------------
# HIDE SIDEBAR
# -----------------------------------

st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

.login-title {
    text-align: center;
}

.login-subtitle {
    text-align: center;
    color: gray;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# TOP BAR
# -----------------------------------

top1, top2 = st.columns([6, 2])

with top1:
    st.empty()  # keeps alignment clean

with top2:
    st.markdown(
        "<span style='color:black; font-weight:600;'>Theme</span>",
        unsafe_allow_html=True
    )

    st.session_state.dark_mode = st.toggle(
        "",
        value=st.session_state.dark_mode
    )
# -----------------------------------
# LOAD THEME
# -----------------------------------

load_theme()

# -----------------------------------
# IF ALREADY LOGGED IN
# -----------------------------------

if st.session_state.get("logged_in", False):

    st.success(
        f"Logged in as {st.session_state.get('user_name', 'User')}"
    )

    st.write(
        st.session_state.get(
            "user_email",
            ""
        )
    )

    if st.button(
        "Go To Dashboard",
        use_container_width=True
    ):
        st.switch_page("app.py")

    st.stop()

# -----------------------------------
# HEADER
# -----------------------------------

st.markdown(
    "<h1 class='login-title'>SaaS Business Analytics Platform</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='login-subtitle'>Business Intelligence • Churn Prediction • Customer Analytics</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------------
# EMAIL / PASSWORD UI
# -----------------------------------

st.subheader("Login")

email = st.text_input(
    "Email Address"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button(
    "Login",
    use_container_width=True
):

    if email and password:

        st.info(
            "Demo Login Enabled. Use Google Sign-In for secure authentication."
        )

    else:

        st.warning(
            "Please enter email and password."
        )

st.markdown("### Or Continue With Google")

# -----------------------------------
# GOOGLE OAUTH
# -----------------------------------

google_login()

st.markdown("---")

st.caption(
    "Secure authentication powered by Google OAuth 2.0"
)