import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📉", layout="centered")


@st.cache_resource
def load_model():
    return joblib.load("churn_model.pkl")


model = load_model()

st.title("📉 Customer Churn Prediction")
st.write("Enter customer details to predict whether the customer is likely to leave the telecom company.")

# ---------------- Customer Information ----------------
st.subheader("Customer Information")
c1, c2 = st.columns(2)
with c1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
with c2:
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.slider("Tenure (months)", 0, 72, 12)

# ---------------- Services ----------------
st.subheader("Services")
c1, c2 = st.columns(2)
with c1:
    phone = st.selectbox("Phone Service", ["Yes", "No"])
with c2:
    if phone == "Yes":
        multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"])
    else:
        multiple_lines = "No phone service"
        st.selectbox("Multiple Lines", ["No phone service"], disabled=True)

internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

addons = ["OnlineSecurity", "OnlineBackup", "DeviceProtection",
          "TechSupport", "StreamingTV", "StreamingMovies"]
addon_values = {}

if internet == "No":
    for a in addons:
        addon_values[a] = "No internet service"
    st.info("Internet add-on services are not available without internet service.")
else:
    c1, c2 = st.columns(2)
    for i, a in enumerate(addons):
        with (c1 if i % 2 == 0 else c2):
            addon_values[a] = st.selectbox(a, ["No", "Yes"])

# ---------------- Billing ----------------
st.subheader("Billing")
c1, c2 = st.columns(2)
with c1:
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
with c2:
    payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check",
                                              "Bank transfer (automatic)", "Credit card (automatic)"])
    monthly = st.number_input("Monthly Charges", min_value=18.0, max_value=120.0, value=70.0, step=0.5)

total = st.number_input("Total Charges", min_value=0.0, value=float(round(tenure * monthly, 2)), step=10.0)

# ---------------- Prediction ----------------
if st.button("Predict churn", type="primary", use_container_width=True):
    input_df = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple_lines,
        "InternetService": internet,
        **addon_values,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }])

    prob = model.predict_proba(input_df)[0, 1]
    pred = model.predict(input_df)[0]

    st.subheader("Result")
    if pred == 1:
        st.error(f"⚠️ This customer is **likely to churn**. Churn probability: **{prob:.1%}**")
    else:
        st.success(f"✅ This customer is **likely to stay**. Churn probability: **{prob:.1%}**")
    st.progress(float(prob))
