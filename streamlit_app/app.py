import streamlit as st
import pandas as pd
from pathlib import Path
from navbar import show_navbar
from theme import load_theme

if not st.session_state.get("logged_in", False):
    st.switch_page("pages/0_Login.py")

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="SaaS Business Analytics Platform",
    page_icon="📊",
    layout="wide"
)

load_theme()
show_navbar()

st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# LOAD CSS
# ---------------------------------------------------

theme_folder = Path(__file__).parent / "themes"

if st.session_state.dark_mode:
    css_file = theme_folder / "dark.css"

    card_bg = "#1C2128"
    text_color = "white"
    border_color = "#30363D"

else:
    css_file = theme_folder / "light.css"

    card_bg = "#F8F9FA"
    text_color = "black"
    border_color = "#D3D3D3"

if css_file.exists():
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

col1, col2 = st.columns([8,1])

with col1:
    st.title("📊 SaaS Business Analytics & Prediction Platform")


# ---------------------------------------------------
# DATASET SELECTION
# ---------------------------------------------------

st.subheader("📁 Dataset Selection")

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ Custom Dataset Loaded")

else:

    df = pd.read_csv(
        "data/raw/customer_subscription_churn_usage_patterns.csv"
    )

    st.info("📊 Using Default SaaS Dataset")

st.session_state["data"] = df

with st.expander("Preview Dataset"):
    st.dataframe(df.head())

st.markdown("""
### Welcome to the Analytics Dashboard

Analyze:

✅ Customer Growth

✅ Revenue Performance

✅ Subscription Trends

✅ Churn Prediction

✅ Customer Health Score

Choose the default dataset or upload your own CSV for analysis.
""")

st.divider()

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

st.subheader("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style="
        background:{card_bg};
        color:{text_color};
        border:1px solid {border_color};
        padding:20px;
        border-radius:12px;
        text-align:center;
    ">
        <h4>👥 Customers</h4>
        <h2>2800</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="
        background:{card_bg};
        color:{text_color};
        border:1px solid {border_color};
        padding:20px;
        border-radius:12px;
        text-align:center;
    ">
        <h4>⚠️ Churn Rate</h4>
        <h2>57.32%</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="
        background:{card_bg};
        color:{text_color};
        border:1px solid {border_color};
        padding:20px;
        border-radius:12px;
        text-align:center;
    ">
        <h4>💰 Monthly Revenue</h4>
        <h2>₹12.16L</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="
        background:{card_bg};
        color:{text_color};
        border:1px solid {border_color};
        padding:20px;
        border-radius:12px;
        text-align:center;
    ">
        <h4>❤️ Health Score</h4>
        <h2>73.48</h2>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# PLATFORM FEATURES
# ---------------------------------------------------

st.subheader("🚀 Platform Features")

feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.info("""
### 📊 Analytics

- Customer Growth
- Revenue Analysis
- Plan Performance
- Churn Monitoring
""")

with feature2:
    st.info("""
### 🤖 AI Predictions

- Churn Prediction
- Customer Risk Detection
- Retention Analysis
- Business Insights
""")

with feature3:
    st.info("""
### 🗄️ Data Management

- PostgreSQL Database
- SQL Analytics
- Interactive Dashboard
- Real-time Reporting
""")

st.divider()

# ---------------------------------------------------
# ABOUT PROJECT
# ---------------------------------------------------

st.subheader("🎯 About This Project")

st.success("""
This SaaS Business Analytics Platform helps management teams make
data-driven decisions regarding:

• Customer Retention

• Revenue Growth

• User Engagement

• Subscription Performance

• Churn Prediction

• Customer Health Monitoring

Built using Python, PostgreSQL, Machine Learning, and Streamlit.
""")

st.info(
    "👈 Use the sidebar to explore all pages and analytics modules."
)