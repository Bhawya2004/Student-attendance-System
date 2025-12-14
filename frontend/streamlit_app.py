import streamlit as st
import requests

st.set_page_config(page_title="Student Dropout Predictor", layout="centered")

st.title("🎓 Student Dropout Risk Prediction")
st.write("Enter student details to predict dropout risk")

# Input fields
age = st.number_input("Age", min_value=10, max_value=25, value=17)
studytime = st.selectbox("Weekly Study Time (1: <2h, 2: 2-5h, 3: 5-10h, 4: >10h)", [1, 2, 3, 4])
failures = st.number_input("Past Failures", min_value=0, max_value=5, value=0)
absences = st.number_input("Absences", min_value=0, max_value=100, value=5)
Medu = st.selectbox("Mother's Education Level (0-4)", [0, 1, 2, 3, 4])
Fedu = st.selectbox("Father's Education Level (0-4)", [0, 1, 2, 3, 4])
internet = st.selectbox("Internet Access (0: No, 1: Yes)", [0, 1])
G1 = st.number_input("Grade G1 (0-20)", min_value=0, max_value=20, value=10)
G2 = st.number_input("Grade G2 (0-20)", min_value=0, max_value=20, value=10)

if st.button("Predict Dropout Risk"):
    payload = {
        "age": age,
        "studytime": studytime,
        "failures": failures,
        "absences": absences,
        "Medu": Medu,
        "Fedu": Fedu,
        "internet": internet,
        "G1": G1,
        "G2": G2
    }

    try:
        # Assuming FastAPI is running locally on port 8000
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            if result["dropout_risk"] == 1:
                st.error(f"⚠️ High Dropout Risk\n\nProbability: {result['risk_probability']*100:.1f}%")
            else:
                st.success(f"✅ Low Dropout Risk\n\nProbability: {result['risk_probability']*100:.1f}%")
        else:
            st.error(f"Error: {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to FastAPI server. Is it running?")
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
