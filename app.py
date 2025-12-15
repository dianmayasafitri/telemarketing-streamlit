import streamlit as st
import pandas as pd
import joblib
import sklearn

@st.cache_resource
def load_model():
    return joblib.load("model_telemarketing_campaign.sav")

def main():

    model = load_model()
    
    st.title("📞 Telemarketing Campaign Prediction")
    st.write("Prediksi apakah nasabah akan subscribe deposito")

    age = st.number_input("Age", 18, 100, 30)
    job = st.selectbox("Job", [
        "admin.", "blue-collar", "technician", "services",
        "management", "retired", "self-employed", "student",
        "unemployed", "entrepreneur"
    ])
    marital = st.selectbox("Marital", ["married", "single", "divorced"])

    education_label_to_value = {
        "Basic 4 Years": "basic.4y",
        "Basic 6 Years": "basic.6y",
        "Basic 9 Years": "basic.9y",
        "High School": "high.school",
        "Professional Course": "professional.course",
        "University Degree": "university.degree",
        "Illiterate": "illiterate",
        "Unknown": "unknown"
    }

    education_label = st.selectbox(
        "Education",
        list(education_label_to_value.keys())
    )
    education = education_label_to_value[education_label]

    balance = st.number_input("Balance", value=1000)
    housing = st.selectbox("Housing Loan", ["yes", "no"])
    loan = st.selectbox("Personal Loan", ["yes", "no"])
    duration = st.number_input("Call Duration (seconds)", value=120)

    input_df = pd.DataFrame([{
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "balance": balance,
        "housing": housing,
        "loan": loan,
        "duration": duration,
        "campaign": 1,
        "default": "no",
        "contact": "cellular",
        "day_of_week": "mon",
        "month": "may",
        "poutcome": "nonexistent",
        "pdays": 999,
        "previous": 0,
        "emp.var.rate": 1.1,
        "cons.price.idx": 93.994,
        "cons.conf.idx": -36.4,
        "euribor3m": 4.857,
        "nr.employed": 5191
    }])

    if st.button("Predict"):
        st.write(f"sklearn runtime version: {sklearn.__version__}")
        pred = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]

        if pred == 1:
            st.success(f"✅ Subscribe ({prob:.2%})")
        else:
            st.error(f"❌ Not Subscribe ({prob:.2%})")

if __name__ == "__main__":
    main()
