import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Churn Predictor", page_icon="📉", layout="centered")

# ---------- Custom styling ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f1123 0%, #1b1e3d 50%, #221c4f 100%);
    color: #eaeaea;
}
h1, h2, h3, .stMarkdown p {
    color: #f5f5f5 !important;
}
div[data-testid="stMetricValue"] {
    color: #ff4b8b;
}
.stButton>button {
    background: linear-gradient(90deg, #ff4b8b, #7b2ff7);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.6em 1.5em;
    font-weight: 600;
    transition: 0.2s;
}
.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 15px rgba(255,75,139,0.5);
}
div[data-baseweb="select"] > div, .stNumberInput input, .stSlider {
    background-color: #262952 !important;
    color: white !important;
    border-radius: 8px;
}
.result-card {
    padding: 1.2em;
    border-radius: 14px;
    margin-top: 1em;
    text-align: center;
    font-size: 1.4em;
    font-weight: 700;
}
.high-risk {
    background: rgba(255, 75, 90, 0.15);
    border: 1px solid #ff4b5a;
    color: #ff8a95;
}
.low-risk {
    background: rgba(75, 255, 170, 0.12);
    border: 1px solid #4bffb0;
    color: #7effc9;
}
</style>
""", unsafe_allow_html=True)

# ---------- Load model ----------
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# ---------- Header ----------
st.markdown("<h1>📉 Customer Churn Predictor</h1>", unsafe_allow_html=True)
st.markdown("Enter a customer's details below to estimate their churn risk.")

st.markdown("---")

# ---------- Inputs ----------
col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0)
    total_charges = st.number_input("Total Charges ($)", 0.0, 9000.0, 1000.0)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])

with col2:
    partner = st.selectbox("Has Partner", ["No", "Yes"])
    dependents = st.selectbox("Has Dependents", ["No", "Yes"])
    paperless = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment = st.selectbox("Payment Method",
                            ["Electronic check", "Mailed check",
                             "Bank transfer (automatic)", "Credit card (automatic)"])
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])

st.markdown("---")

# ---------- Prediction ----------
if st.button("🔮 Predict Churn Risk"):
    row = pd.DataFrame(0.0, index=[0], columns=columns)

    row["tenure"] = tenure
    row["MonthlyCharges"] = monthly_charges
    row["TotalCharges"] = total_charges
    row["SeniorCitizen"] = 1 if senior == "Yes" else 0

    def set_dummy(col_name):
        if col_name in row.columns:
            row[col_name] = 1

    if contract == "One year":
        set_dummy("Contract_One year")
    elif contract == "Two year":
        set_dummy("Contract_Two year")

    if internet == "Fiber optic":
        set_dummy("InternetService_Fiber optic")
    elif internet == "No":
        set_dummy("InternetService_No")

    if partner == "Yes":
        set_dummy("Partner_Yes")
    if dependents == "Yes":
        set_dummy("Dependents_Yes")
    if paperless == "Yes":
        set_dummy("PaperlessBilling_Yes")

    if payment == "Credit card (automatic)":
        set_dummy("PaymentMethod_Credit card (automatic)")
    elif payment == "Electronic check":
        set_dummy("PaymentMethod_Electronic check")
    elif payment == "Mailed check":
        set_dummy("PaymentMethod_Mailed check")

    if online_security == "Yes":
        set_dummy("OnlineSecurity_Yes")
    elif online_security == "No internet service":
        set_dummy("OnlineSecurity_No internet service")

    if tech_support == "Yes":
        set_dummy("TechSupport_Yes")
    elif tech_support == "No internet service":
        set_dummy("TechSupport_No internet service")

    num_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
    row[num_cols] = scaler.transform(row[num_cols])

    prob = model.predict_proba(row)[0][1]

    st.markdown(f"<h2 style='text-align:center;'>Churn Probability: {prob:.0%}</h2>",
                unsafe_allow_html=True)

    if prob > 0.5:
        st.markdown(f"<div class='result-card high-risk'>⚠️ High risk of churn</div>",
                    unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='result-card low-risk'>✅ Low risk of churn</div>",
                    unsafe_allow_html=True)

    with st.expander("See what was sent to the model"):
        st.write(row)