# Health Insurance Cost Prediction

A Streamlit-based insurance analytics platform for predicting healthcare costs and exploring insurance data trends.

## Overview

This project includes a user-friendly web app for:
- estimating individual insurance costs using a trained machine learning model
- visualizing insurance claim trends and feature importance
- exploring the impact of factors like age, BMI, smoking status, and region

## Features

- **Insurance Prediction** page
  - Takes user inputs such as age, BMI, blood pressure, gender, smoker status, diabetic status, and number of children
  - Predicts estimated insurance cost using a trained model
  - Displays risk level based on the predicted value

- **Data Analytics Dashboard** page
  - Shows histograms, scatter plots, bar charts, and a correlation matrix
  - Visualizes claim behavior for smokers vs non-smokers
  - Displays model feature importance

- **Styled landing page** with an overview and navigation guidance
- **Power BI dashboard** for interactive reporting and executive analytics

## Project Structure

- `app.py` — main Streamlit landing page
- `pages/1_Insurance_Prediction.py` — insurance cost prediction input form and results
- `pages/2_Data_Analytics_Dashboard.py` — interactive analytics dashboard
- `insurance.csv` — raw insurance dataset
- `insurance_with_predictions.csv` — dataset with model predictions included
- `best_model.pkl` — trained model file
- `scaler.pkl` — scaler used for preprocessing
- `label_encoders.pkl` — any label encoders used by the model
- `requirements.txt` — Python dependencies
- `health insurance Dashboard.pbix` — Power BI dashboard file for additional analytics and reporting

## Setup

1. Create a Python environment (optional but recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the App

From the project root, run:

```bash
streamlit run Overview.py
```

Then open the local URL shown in the terminal.

## Notes

- If the sidebar does not reopen after collapsing, ensure header visibility is not hidden by custom CSS.
- Adjust BMI and blood pressure ranges in `pages/1_Insurance_Prediction.py` if needed for your data.

## Acknowledgements

Built with Streamlit, Plotly, pandas, and scikit-learn.
