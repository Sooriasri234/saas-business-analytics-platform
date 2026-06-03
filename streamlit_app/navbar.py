import streamlit as st

def show_navbar():

    # Hide Sidebar
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display:none;
    }

    [data-testid="collapsedControl"] {
        display:none;
    }
    </style>
    """, unsafe_allow_html=True)

    col1,col2,col3,col4,col5,col6,col7 = st.columns(7)

    with col1:
        if st.button("Dashboard", use_container_width=True):
            st.switch_page("pages/1_Dashboard.py")

    with col2:
        if st.button("Business Insights", use_container_width=True):
            st.switch_page("pages/2_Business_Insights.py")

    with col3:
        if st.button("Churn Prediction", use_container_width=True):
            st.switch_page("pages/3_Churn_Prediction.py")

    with col4:
        if st.button("Customer Health", use_container_width=True):
            st.switch_page("pages/4_Customer_Health.py")

    with col5:
        if st.button("AI Recommendations", use_container_width=True):
            st.switch_page("pages/5_AI_Recommendations.py")

    with col6:
        if st.button("Email Reports", use_container_width=True):
            st.switch_page("pages/6_Email_Reports.py")

    with col7:
        if st.button("Logout", use_container_width=True):

            st.session_state.logged_in = False

            if "user_name" in st.session_state:
                del st.session_state["user_name"]

            if "user_email" in st.session_state:
                del st.session_state["user_email"]

            st.switch_page("pages/0_Login.py")

    st.divider()