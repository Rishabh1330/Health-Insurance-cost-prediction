import streamlit as st

st.set_page_config(
    page_title="Insurance Analytics Platform",
    page_icon="💰",
    layout="wide"
)

st.markdown(
    """
    <style>
    #MainMenu, footer {visibility: hidden;}
    header {
        visibility: visible;
    }
    .stApp {
        background: linear-gradient(135deg, #08101f 0%, #111827 45%, #08161f 100%);
        color: #f8fafc;
    }
    .hero {
        padding: 2rem 1.5rem;
        border-radius: 30px;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(16px);
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.35);
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
        color: #ffffff;
    }
    .hero p {
        color: #d1d5db;
        font-size: 1.05rem;
        line-height: 1.8;
    }
    .feature-card {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 24px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        min-height: 190px;
    }
    .feature-card h3 {
        margin-top: 0;
        color: #ffffff;
    }
    .feature-card p {
        color: #cbd5e1;
    }
    .accent {
        color: #22d6ac;
        font-weight: 700;
    }
    .sidebar-hint {
        background: rgba(0, 201, 167, 0.12);
        border-radius: 18px;
        padding: 1rem;
        color: #e2e8f0;
        border: 1px solid rgba(0, 201, 167, 0.2);
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
    .sidebar-panel p, .sidebar-panel li {
        color: #cbd5e1;
    }
    .sidebar-panel li {
        margin-bottom: 0.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="hero">'
    '<h1>💰 Health Insurance Analytics Platform</h1>'
    '<p>Explore insurance cost prediction, analyze real-world claims data, and understand the key drivers behind policy pricing — all in one elegant dashboard.</p>'
    '</div>',
    unsafe_allow_html=True,
)

left, right = st.columns([3, 1])

with left:
    st.markdown(
        '<div class="feature-card">'
        '<h3>🔮 Insurance Cost Prediction</h3>'
        '<p>Use a trained machine learning model to estimate insurance costs based on personal health and lifestyle inputs.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="feature-card" style="margin-top: 1rem;">'
        '<h3>📊 Data Analytics Dashboard</h3>'
        '<p>Visualize trends, compare smoker vs non-smoker claims, and inspect how age, BMI, and region impact insurance costs.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="feature-card" style="margin-top: 1rem;">'
        '<h3>🧠 Model Insights</h3>'
        '<p>Learn which features most influence the model and gain transparency into cost drivers with feature importance insights.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

with right:
    st.markdown('<div class="sidebar-hint"><strong class="accent">Tip:</strong> Use the sidebar to jump between Prediction and Analytics with ease.</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-hint" style="margin-top: 1rem;"><strong class="accent">Best practice:</strong> enter realistic age, BMI and lifestyle values to get more meaningful predictions.</div>', unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-panel"><h2>Overview</h2><ul><li>Prediction</li><li>Data Analytics Dashboard</li><li>Model Insights</li></ul></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-panel"><h2>Quick Tips</h2><p>Start with the Prediction page, then compare results in the Analytics Dashboard for deeper insight.</p></div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    '## Getting Started\n' 
    '- Select **Prediction** to estimate individual insurance costs.\n' 
    '- Open **Data Analytics Dashboard** to explore visual trends.\n' 
    '- Use insights to understand key insurance risk factors.\n'
)

st.info("Navigate using the sidebar on the left to access Prediction and Analytics Dashboard.")
import streamlit as st

st.set_page_config(
    page_title="Insurance Analytics Platform",
    page_icon="💰",
    layout="wide"
)

st.markdown(
    """
    <style>
    #MainMenu, footer {visibility: hidden;}
    header {
        visibility: visible;
    }
    .stApp {
        background: linear-gradient(135deg, #08101f 0%, #111827 45%, #08161f 100%);
        color: #f8fafc;
    }
    .hero {
        padding: 2rem 1.5rem;
        border-radius: 30px;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(16px);
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.35);
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
        color: #ffffff;
    }
    .hero p {
        color: #d1d5db;
        font-size: 1.05rem;
        line-height: 1.8;
    }
    .feature-card {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 24px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        min-height: 190px;
    }
    .feature-card h3 {
        margin-top: 0;
        color: #ffffff;
    }
    .feature-card p {
        color: #cbd5e1;
    }
    .accent {
        color: #22d6ac;
        font-weight: 700;
    }
    .sidebar-hint {
        background: rgba(0, 201, 167, 0.12);
        border-radius: 18px;
        padding: 1rem;
        color: #e2e8f0;
        border: 1px solid rgba(0, 201, 167, 0.2);
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
    .sidebar-panel p, .sidebar-panel li {
        color: #cbd5e1;
    }
    .sidebar-panel li {
        margin-bottom: 0.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="hero">'
    '<h1>💰 Health Insurance Analytics Platform</h1>'
    '<p>Explore insurance cost prediction, analyze real-world claims data, and understand the key drivers behind policy pricing — all in one elegant dashboard.</p>'
    '</div>',
    unsafe_allow_html=True,
)

left, right = st.columns([3, 1])

with left:
    st.markdown(
        '<div class="feature-card">'
        '<h3>🔮 Insurance Cost Prediction</h3>'
        '<p>Use a trained machine learning model to estimate insurance costs based on personal health and lifestyle inputs.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="feature-card" style="margin-top: 1rem;">'
        '<h3>📊 Data Analytics Dashboard</h3>'
        '<p>Visualize trends, compare smoker vs non-smoker claims, and inspect how age, BMI, and region impact insurance costs.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="feature-card" style="margin-top: 1rem;">'
        '<h3>🧠 Model Insights</h3>'
        '<p>Learn which features most influence the model and gain transparency into cost drivers with feature importance insights.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

with right:
    st.markdown('<div class="sidebar-hint"><strong class="accent">Tip:</strong> Use the sidebar to jump between Prediction and Analytics with ease.</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-hint" style="margin-top: 1rem;"><strong class="accent">Best practice:</strong> enter realistic age, BMI and lifestyle values to get more meaningful predictions.</div>', unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-panel"><h2>About this page</h2><p>This overview page explains the platform: use the menu to switch between insurance prediction, analytics, and model insight pages.</p></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-panel"><h2>Navigate</h2><ul><li>🔮 Insurance Prediction</li><li>📊 Analytics Dashboard</li><li>🧠 Model Insights</li></ul></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-panel"><h2>Need help?</h2><p>Start with the Prediction page for a cost estimate, then use the Analytics Dashboard for trend exploration.</p></div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    '## Getting Started\n' 
    '- Select **Prediction** to estimate individual insurance costs.\n' 
    '- Open **Data Analytics Dashboard** to explore visual trends.\n' 
    '- Use insights to understand key insurance risk factors.\n'
)

st.info("Navigate using the sidebar on the left to access Prediction and Analytics Dashboard.")
