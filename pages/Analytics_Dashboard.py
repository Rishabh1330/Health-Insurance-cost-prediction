import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
st.set_page_config(page_title="Data Analytics Dashboard", layout="wide")

# Load the data
filtered_df = pd.read_csv("insurance_with_predictions.csv")  # Replace with your actual data path

# Load feature importance from the model
model = joblib.load("best_model.pkl")  # Replace with your actual model path
importance_df = pd.DataFrame({
    "Feature": model.feature_names_in_,
    "Importance": model.feature_importances_
}).sort_values("Importance", ascending=False)
st.markdown("""
<style>

/* Background */
.main {
    background: linear-gradient(135deg, #0E1117, #111827);
    color: white;
}

/* Headings */
h1, h2, h3 {
    background: -webkit-linear-gradient(#00C9A7, #4FACFE);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* KPI Cards (Glassmorphism) */
.stMetric {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    padding: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(0,201,167,0.2);
    transition: 0.3s;
}

.stMetric:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(0,201,167,0.6);
}

/* Sidebar */
.css-1d391kg {
    background: rgba(17,24,39,0.8);
}
header {
    visibility: visible !important;
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

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: #00C9A7;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)
def insane_theme(fig):
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        title_x=0.25,
        margin=dict(l=10, r=10, t=50, b=10),
        hoverlabel=dict(
            bgcolor="#111827",
            font_size=14,
            font_family="Arial"
        )
    )
    return fig
fig1 = px.histogram(
    filtered_df,
    x="claim",
    nbins=30,
    title="💰 Claim Distribution",
    opacity=0.9
)

fig1.update_traces(
    marker=dict(
        color="#00C9A7",
        line=dict(width=1, color="white")
    )
)

fig1 = insane_theme(fig1)

st.sidebar.markdown('<div class="sidebar-panel"><h2>Dashboard</h2><ul><li>Overview</li><li>Claim Trends</li><li>Feature Importance</li></ul></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-panel"><h2>Tips</h2><p>Use the charts to compare claim behavior for smokers vs non-smokers and identify high-risk segments.</p></div>', unsafe_allow_html=True)

st.plotly_chart(fig1, use_container_width=True, key="hist_claim")

fig2 = px.scatter(
    filtered_df,
    x="age",
    y="claim",
    color="smoker",
    size="bmi",
    hover_data=["children","region"],
    title="📊 Age vs Claim (Behavior Analysis)",
    color_discrete_map={
        "Yes": "#FF4B4B",
        "No": "#00C9A7"
    }
)

fig2.update_traces(
    marker=dict(
        opacity=0.8,
        line=dict(width=1, color="white")
    )
)

fig2 = insane_theme(fig2)

st.plotly_chart(fig2, use_container_width=True, key="scatter_age_claim")
smoker_claim = filtered_df.groupby("smoker")["claim"].mean().reset_index()

fig3 = px.bar(
    smoker_claim,
    x="smoker",
    y="claim",
    color="smoker",
    text_auto=".2s",
    title="🚬 Smoking Impact on Claims",
    color_discrete_map={
        "Yes": "#FF4B4B",
        "No": "#00C9A7"
    }
)

fig3.update_traces(
    textposition="outside"
)

fig3 = insane_theme(fig3)

st.plotly_chart(fig3, use_container_width=True, key="bar_smoker_claim")
corr = filtered_df.corr(numeric_only=True)

fig4 = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    color_continuous_scale=["#FF4B4B","#111827","#00C9A7"],
    title="🔍 Correlation Matrix"
)

fig4 = insane_theme(fig4)

st.plotly_chart(fig4, use_container_width=True, key="corr_matrix")
fig5 = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    color_continuous_scale=["#00C9A7","#4FACFE"],
    title="⚙️ Feature Importance"
)

fig5.update_layout(
    yaxis=dict(categoryorder="total ascending")
)

fig5 = insane_theme(fig5)

st.plotly_chart(fig5, use_container_width=True, key="feature_importance")
st.markdown("## 📊 Advanced Analytics Dashboard")

col1, col2 = st.columns([2,1])

with col1:
    st.plotly_chart(fig2, use_container_width=True, key="scatter_age_claim_col1")

with col2:
    st.plotly_chart(fig3, use_container_width=True, key="bar_smoker_claim_col2")

st.plotly_chart(fig1, use_container_width=True, key="hist_claim_bottom")

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(fig4, use_container_width=True, key="corr_matrix_col3")

with col4:
    st.plotly_chart(fig5, use_container_width=True, key="feature_importance_col4")
st.markdown("""
<div style="
background: rgba(255,255,255,0.05);
padding: 20px;
border-radius: 15px;
box-shadow: 0 0 20px rgba(0,201,167,0.3);
">

<h3>📌 Key Insights</h3>

<ul>
<li>🚬 Smokers have significantly higher insurance claims</li>
<li>⚖️ BMI strongly influences healthcare costs</li>
<li>📈 Age positively correlates with claim amount</li>
<li>💡 Lifestyle factors dominate insurance pricing</li>
</ul>

</div>
""", unsafe_allow_html=True)

