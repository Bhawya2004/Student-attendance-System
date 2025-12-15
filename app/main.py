from fastapi import FastAPI
import joblib
import numpy as np
from app.schema import StudentData
import os
import csv
from datetime import datetime



app = FastAPI(title="Student Dropout Prediction API")
# Get the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the model file (one level up, then into model folder)
MODEL_PATH = os.path.join(BASE_DIR, "../model/student_attendance_trainned_model.pkl")

model = joblib.load(MODEL_PATH)
LOG_FILE = "monitoring/logs/predictions.csv"

def log_prediction(data, prediction, probability):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            data.age,
            data.studytime,
            data.failures,
            data.absences,
            data.Medu,
            data.Fedu,
            data.internet,
            data.G1,
            data.G2,
            prediction,
            probability,
            datetime.now()
        ])


@app.get("/")
def home():
    return {"message": "Student Dropout Prediction API is running"}

@app.post("/predict")
def predict_dropout(data: StudentData):
    input_data = np.array([[
        data.age,
        data.studytime,
        data.failures,
        data.absences,
        data.Medu,
        data.Fedu,
        data.internet,
        data.G1,
        data.G2
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    log_prediction(data, prediction, probability)

    

    return {
        "dropout_risk": int(prediction),
        "risk_probability": round(float(probability), 2)
    }
