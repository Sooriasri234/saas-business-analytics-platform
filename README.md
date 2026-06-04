# SaaS Business Analytics & Prediction Platform

## Overview

The SaaS Business Analytics & Prediction Platform is a data-driven web application developed using Python, Streamlit, PostgreSQL, Machine Learning, and Google OAuth Authentication.

The platform helps businesses analyze customer behavior, monitor subscription performance, predict customer churn, evaluate customer health, and generate actionable business recommendations.

Users can either analyze the default SaaS dataset or upload their own CSV dataset for customized business insights.

---

## Features

### Secure Authentication

* Google OAuth 2.0 Login
* Email and Password Login Interface
* Session Management
* Secure User Access Control

### Dataset Management

* Upload Custom CSV Datasets
* Analyze Built-in SaaS Dataset
* Automatic Dataset Preview
* Dynamic Data Processing

### Executive Dashboard

* Total Customer Analysis
* Churn Rate Monitoring
* Revenue Analysis
* Customer Health Metrics
* Interactive KPI Cards

### Business Insights

* Customer Distribution Analysis
* Subscription Trend Analysis
* Customer Risk Segmentation
* Interactive Visualizations
* Data-Driven Insights

### Churn Prediction

* Machine Learning Based Prediction
* Customer Risk Detection
* Churn Probability Calculation
* Customer Retention Support

### Customer Health Score

* Customer Engagement Evaluation
* Health Score Calculation
* Risk Classification
* Customer Activity Monitoring

### AI Business Recommendations

* Intelligent Business Suggestions
* Churn Reduction Strategies
* Revenue Growth Recommendations
* Customer Retention Insights

### Email Reporting

* SMTP Email Integration
* Automated Business Reports
* Executive Summary Reports
* Share Analytics Results via Email

### User Interface

* Professional SaaS Dashboard Design
* Dark Theme Support
* Light Theme Support
* Responsive Layout
* Navigation Bar Based Interface
* Sidebar-Free User Experience

---

## Technologies Used

### Frontend

* Streamlit
* HTML
* CSS

### Backend

* Python

### Database

* PostgreSQL

### Machine Learning

* Scikit-Learn
* Joblib
* Pandas
* NumPy

### Data Visualization

* Plotly
* Matplotlib

### Authentication

* Google OAuth 2.0

### Email Services

* SMTP

---

## Installation

### Clone Repository

```
cd saas-business-analytics-platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
cd streamlit_app

streamlit run app.py
```

---

## Google OAuth Configuration

1. Create a Google Cloud Project.
2. Configure the OAuth Consent Screen.
3. Enable Google People API.
4. Create OAuth Client Credentials.
5. Add Authorized Redirect URIs.
6. Store credentials inside `.streamlit/secrets.toml`.
---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Model Training
5. Churn Prediction
6. Customer Risk Analysis
7. Business Recommendation Generation

---

## Key Business Metrics

* Total Customers
* Churn Rate
* Revenue Performance
* Customer Health Score
* Customer Retention Rate
* Subscription Performance
* Customer Engagement

---

## Future Enhancements

* Real-Time Analytics
* Predictive Revenue Forecasting
* Advanced AI Recommendations
* Automated Scheduled Reports
* Multi-User Role Management
* Cloud Database Integration
* API Integration
* Advanced Dashboard Customization

---

## Project Outcomes

This platform helps organizations:

* Reduce Customer Churn
* Improve Customer Retention
* Increase Revenue Growth
* Monitor Customer Health
* Make Data-Driven Decisions
* Generate Actionable Business Insights

---

