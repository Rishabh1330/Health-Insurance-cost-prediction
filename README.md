# 🏥 Health Insurance Cost Prediction & Analytics Platform

A full-stack **data analytics and machine learning platform** built using **Streamlit and Power BI** for predicting healthcare costs and exploring insurance data trends through interactive dashboards.

---

## 📌 Overview

This project combines **Machine Learning, Data Analytics, and Business Intelligence** to:

* Predict individual insurance costs using a trained ML model
* Analyze insurance data to uncover trends and patterns
* Provide interactive dashboards for better decision-making

The platform consists of:

* 🌐 **Streamlit Web Application** (for predictions & analytics)
* 📊 **Power BI Dashboard** (for advanced business intelligence reporting)

---

## 🚀 Key Features

### 🔮 Insurance Cost Prediction

* User-friendly input form for:

  * Age, BMI, Blood Pressure
  * Gender, Smoker Status, Diabetic Status
  * Number of Children
* Predicts estimated insurance cost using ML model
* Displays **risk level classification**

---

### 📊 Data Analytics Dashboard (Streamlit)

* Interactive visualizations:

  * Claim distribution (Histogram)
  * Age vs Claim (Scatter plot)
  * Smoker vs Non-smoker comparison (Bar chart)
  * Correlation heatmap
* Feature importance visualization
* Dynamic filtering (Age, BMI)

---

### 📈 Power BI Dashboard (Business Intelligence Layer)

* Professional **executive-level dashboard**
* KPI Cards:

  * Total Claims
  * Average Charges
  * Customer Segmentation
* Advanced analytics:

  * Claim trends by region, age group, and lifestyle
  * Smoker vs non-smoker financial impact
  * High-risk customer identification
* Drill-down and interactive filtering capabilities

📂 File: `health insurance Dashboard.pbix`

---

### 🎨 UI/UX Highlights

* Modern **dark theme dashboard**
* Glassmorphism UI design
* Responsive layout
* Interactive charts using Plotly

---

## 🧠 Machine Learning

* Model Used: *(e.g., Random Forest / Linear Regression)*
* Target Variable: Insurance Charges
* Features:

  * Age, BMI, Children
  * Smoking Status
  * Blood Pressure
  * Lifestyle indicators

### ⚙️ Preprocessing

* Label Encoding
* Feature Scaling
* Data Cleaning

---

## 📂 Project Structure

```
health-insurance-app/
│
├── app.py
├── insurance.csv
├── insurance_with_predictions.csv
├── best_model.pkl
├── scaler.pkl
├── label_encoders.pkl
├── requirements.txt
│
├── pages/
│     1_Insurance_Prediction.py
│     2_Data_Analytics_Dashboard.py
│
├── powerbi/
│     health insurance Dashboard.pbix
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment (Optional)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the local URL shown in the terminal.

---

## 📊 Key Insights

* 🚬 Smokers incur significantly higher insurance costs
* ⚖️ BMI strongly influences healthcare expenses
* 📈 Age shows positive correlation with claim amounts
* 💡 Lifestyle factors are major drivers of insurance pricing

---

## 💼 Business Value

* Helps insurers in **risk assessment**
* Improves **premium pricing strategies**
* Enables **data-driven decision making**
* Identifies **high-risk customers**

---

## ⚠️ Notes

* Ensure all `.pkl` files are present before running
* Adjust input ranges if needed in prediction page
* Power BI file can be opened using Power BI Desktop

---

## 🙌 Acknowledgements

Built using:

* Python
* Streamlit
* Plotly
* Pandas
* Scikit-learn
* Power BI

---

## 📬 Author

**Rishabh Verma**
B.Tech Computer Science | Data Analytics Enthusiast
📍 New Delhi, India

🔗 LinkedIn: https://www.linkedin.com/in/rishabh-verma-58489026a/
