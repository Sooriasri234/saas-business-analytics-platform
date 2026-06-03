import streamlit as st
import requests
from streamlit_oauth import OAuth2Component

CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]
REDIRECT_URI = st.secrets["REDIRECT_URI"]

AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"

oauth2 = OAuth2Component(
    CLIENT_ID,
    CLIENT_SECRET,
    AUTHORIZE_URL,
    TOKEN_URL,
)

SCOPES = [
    "openid",
    "email",
    "profile"
]


def google_login():

    result = oauth2.authorize_button(
        name="🔐 Sign in with Google",
        icon="https://www.google.com/favicon.ico",
        redirect_uri=REDIRECT_URI,
        scope=" ".join(SCOPES),
        key="google_login",
        use_container_width=True,
    )

    if result and "token" in result:

        access_token = result["token"]["access_token"]

        response = requests.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        if response.status_code == 200:

            user_info = response.json()

            st.session_state.logged_in = True
            st.session_state.user_name = user_info.get("name", "User")
            st.session_state.user_email = user_info.get("email", "")

            st.session_state.logged_in = True
            st.rerun()