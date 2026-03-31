import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Insurance Cost Prediction", layout="wide")

st.markdown(
    """
    <style>
    #MainMenu, footer {visibility: hidden;}
    header {visibility: visible;}
    .css-1d391kg {background: rgba(17,24,39,0.82) !important;}
    .stApp {
        background: linear-gradient(135deg, #0B1120 0%, #121827 45%, #0C152A 100%);
        color: #f8fafc;
    }
    .stForm {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(12px);
    }
    .stButton>button {
        background: #00C9A7;
        color: #111827;
        font-weight: 700;
        border: none;
    }
    .stButton>button:hover {
        background: #22d6ac;
    }
    .stMetric > div {
        background: rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 1rem 1.2rem;
    }
    .form-label {
        color: #e2e8f0;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(7, 18, 37, 0.96), rgba(12, 22, 45, 0.98));
        border-right: 1px solid rgba(255,255,255,0.08);
    }
    .sidebar-panel {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255,255,255,0.12);
    }
    .sidebar-panel h2 {
        color: #ffffff;
        margin-top: 0;
    }
    .sidebar-panel ul {
        list-style: none;
        padding-left: 0;
        margin: 0.5rem 0 0 0;
    }
    .sidebar-panel li {
        margin-bottom: 0.5rem;
        color: #cbd5e1;
    }
    .sidebar-panel li::before {
        content: '•';
        color: #00C9A7;
        display: inline-block;
        width: 1rem;
    }
    .sidebar-panel p {
        color: #cbd5e1;
        margin: 0.5rem 0 0 0;
    }
    .sidebar-label {
        color: #22d6ac;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("# 🔮 Insurance Cost Prediction")
st.markdown("## Get a fast estimate for your healthcare expenses with a smart, personalized model.")

with st.container():
    left, right = st.columns([2, 1])

    with left:
        with st.form("prediction_form"):
            col1, col2 = st.columns(2)

            with col1:
                age = st.number_input("Age", 0, 100, 30, key="age")
                bmi = st.number_input("BMI", 10.0, 60.0, 25.0, step=0.1, format="%.1f", key="bmi")
                children = st.number_input("Number of Children", 0, 8, 0, key="children")

            with col2:
                bloodpressure = st.number_input("Blood Pressure", 60, 200, 120, key="bloodpressure")
                gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
                diabetic = st.selectbox("Diabetic", ["No", "Yes"], key="diabetic")
                smoker = st.selectbox("Smoker", ["No", "Yes"], key="smoker")

            submit = st.form_submit_button("Predict Insurance Cost")

    with right:
        st.markdown("### Why this matters")
        st.markdown(
            """
            - 📊 Uses historical claims data to estimate costs.
            - 🧠 Encodes lifestyle and health measurements.
            - ⚙️ Designed for fast, interpretable predictions.
            - ✨ Works best for adults with standard insurance factors.
            """
        )
        st.write("")
        st.markdown(
            "<div style='background: rgba(0, 201, 167, 0.12); padding: 1rem; border-radius: 18px;'>"
            "<strong>Tip:</strong> Try different BMI and smoker values to see how costs change." 
            "</div>",
            unsafe_allow_html=True,
        )

st.sidebar.markdown('<div class="sidebar-panel"><h2>Overview</h2><ul><li>🔮 Prediction</li><li>📊 Data Analytics Dashboard</li><li>🧠 Model Insights</li></ul></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-panel"><h2>Tips</h2><p>Use realistic values for age, BMI, and smoking status to get the most meaningful prediction.</p></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-panel"><span class="sidebar-label">Need help?</span><p>Refresh the page to reset inputs, or switch to the analytics page to compare trends.</p></div>', unsafe_allow_html=True)

if submit:
    scaler = joblib.load("scaler.pkl")
    model = joblib.load("best_model.pkl")

    gender_encoded = 1 if gender == "Male" else 0
    diabetic_encoded = 1 if diabetic == "Yes" else 0
    smoker_encoded = 1 if smoker == "Yes" else 0

    input_data = pd.DataFrame(
        {
            "age": [age],
            "bmi": [bmi],
            "children": [children],
            "bloodpressure": [bloodpressure],
            "smoker": [smoker_encoded],
            "diabetic": [diabetic_encoded],
            "gender": [gender_encoded],
        }
    )

    num_cols = ["age", "bmi", "children", "bloodpressure"]
    input_data[num_cols] = scaler.transform(input_data[num_cols])

    prediction = model.predict(input_data)[0]

    result_col1, result_col2, result_col3 = st.columns(3)
    result_col1.metric("Estimated Cost", f"${prediction:,.2f}")
    result_col2.metric("Smoker", smoker)
    result_col3.metric("Diabetic", diabetic)

    if prediction > 20000:
        st.error("⚠️ High Insurance Risk")
    elif prediction > 10000:
        st.warning("⚠️ Medium Insurance Risk")
    else:
        st.success("✅ Low Insurance Risk")
