import streamlit as st
from pathlib import Path

def load_theme():

    # Initialize Dark Mode State
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False


        st.markdown("---")

        # Logout Button
        if st.button(
            "Logout",
            use_container_width=True
        ):

            st.session_state.authenticated = False

            st.switch_page(
                "pages/0_Login.py"
            )

    # Theme Folder
    theme_folder = Path(__file__).parent / "themes"

    # Select CSS
    if st.session_state.dark_mode:
        css_file = theme_folder / "dark.css"
    else:
        css_file = theme_folder / "light.css"

    # Load CSS
    if css_file.exists():
        with open(css_file, encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )