import streamlit as st
import pandas as pd
import joblib

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ======================
# CUSTOM CSS (🔥 FINAL FIXED UI)
# ======================
st.markdown("""
<style>

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #020617;
}

/* HEADINGS (🔥 FIXED VISIBILITY) */
h1, h2, h3 {
    color: #ffffff !important;
    font-weight: 700;
}

/* SUBTEXT */
p {
    color: #cbd5f5;
}

/* CARDS (STRONGER VISIBILITY) */
.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 16px;
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* INPUT FIELDS */
input, select {
    color: white !important;
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
}

/* METRIC CARDS */
div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 12px;
}

/* METRIC LABEL */
div[data-testid="stMetricLabel"] {
    color: #cbd5f5 !important;
}

/* METRIC VALUE (🔥 FIXED) */
div[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 30px;
    font-weight: bold;
}

/* SECTION TITLES */
.section-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #ffffff;
}

/* DIVIDER */
hr {
    border: 1px solid rgba(255,255,255,0.15);
}

</style>
""", unsafe_allow_html=True)

# ======================
# LOAD MODEL
# ======================
@st.cache_resource
def load_model():
    return joblib.load("churn_pipeline.pkl")

model = load_model()

# ======================
# TITLE
# ======================
st.title("📊 Customer Churn Prediction System")
st.markdown("### 🚀 Predict whether a customer is likely to churn")
st.markdown("---")

# ======================
# LAYOUT
# ======================
col1, col2 = st.columns(2)

# ======================
# LEFT CARD
# ======================
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">👤 Customer Demographics</div>', unsafe_allow_html=True)

    age = st.slider("Age", 18, 80, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", [0, 1])
    dependents = st.number_input("Number of Dependents", 0, 10, 0)
    senior = st.selectbox("Senior Citizen", [0, 1])

    st.markdown('<div class="section-title">📡 Services</div>', unsafe_allow_html=True)

    internet = st.selectbox("Internet Type", ["None", "Basic", "Premium"])
    phone = st.selectbox("Phone Service", [0, 1])
    multiple = st.selectbox("Multiple Lines", [0, 1])
    streaming_tv = st.selectbox("Streaming TV", [0, 1])
    streaming_movies = st.selectbox("Streaming Movies", [0, 1])

    st.markdown('</div>', unsafe_allow_html=True)

# ======================
# RIGHT CARD
# ======================
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">💰 Account & Usage</div>', unsafe_allow_html=True)

    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    monthly_charge = st.number_input("Monthly Charge", 0.0, 10000.0, 100.0)
    total_revenue = st.number_input("Total Revenue", 0.0, 100000.0, 1000.0)

    contract = st.selectbox("Contract", ["Month-to-Month", "One Year", "Two Year"])
    payment = st.selectbox("Payment Method", ["Credit Card", "Bank Withdrawal", "Mailed Check"])

    offer = st.selectbox("Offer", ["None", "Basic", "Premium"])

    st.markdown('<div class="section-title">📊 Behavior</div>', unsafe_allow_html=True)

    referrals = st.number_input("Number of Referrals", 0, 20, 0)
    unlimited = st.selectbox("Unlimited Data", [0, 1])
    under30 = st.selectbox("Under 30", [0, 1])

    st.markdown('</div>', unsafe_allow_html=True)

# ======================
# INPUT DATA
# ======================
input_data = {
    "Age": age,
    "Avg Monthly GB Download": 10,
    "Avg Monthly Long Distance Charges": 10,
    "CLTV": 2000,
    "Device Protection Plan": 1,
    "Internet Service": 1,
    "Married": married,
    "Monthly Charge": monthly_charge,
    "Multiple Lines": multiple,
    "Number of Dependents": dependents,
    "Number of Referrals": referrals,
    "Online Backup": 1,
    "Online Security": 1,
    "Paperless Billing": 1,
    "Phone Service": phone,
    "Population": 50000,
    "Premium Tech Support": 1,
    "Senior Citizen": senior,
    "Streaming Movies": streaming_movies,
    "Streaming Music": 1,
    "Streaming TV": streaming_tv,
    "Tenure in Months": tenure,
    "Total Extra Data Charges": 0,
    "Total Long Distance Charges": 100,
    "Total Refunds": 0,
    "Total Revenue": total_revenue,
    "Under 30": under30,
    "Unlimited Data": unlimited,
    "Contract": contract,
    "Gender": gender,
    "Internet Type": internet,
    "Offer": offer,
    "Payment Method": payment
}

input_df = pd.DataFrame([input_data])

# ======================
# PREDICT
# ======================
st.markdown("---")

if st.button("🚀 Predict Churn"):

    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.markdown("## 📢 Prediction Result")

    if pred == 1:
        st.markdown(f"""
        <div style="background: rgba(255,0,0,0.25); padding:20px; border-radius:12px;">
        ⚠️ <b style='color:#ff4d4d;'>High Risk: Customer likely to churn</b>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background: rgba(0,255,0,0.2); padding:20px; border-radius:12px;">
        ✅ <b style='color:#4ade80;'>Low Risk: Customer not likely to churn</b>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📊 Confidence Score")
    st.progress(float(prob))

    colA, colB = st.columns(2)
    colA.metric("Churn Probability", f"{prob:.2%}")
    colB.metric("Model Confidence", f"{(prob if pred==1 else 1-prob):.2%}")

# ======================
# FOOTER
# ======================
st.markdown("---")
st.markdown("✨ Built with Streamlit | ML Project 🚀")