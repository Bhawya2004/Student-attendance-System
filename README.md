# Student Dropout Prediction System

A Machine Learning-powered REST API and Frontend for predicting student dropout risk. This project uses a LightGBM model served via FastAPI, a Streamlit frontend for user interaction, and is containerized with Docker for easy deployment.

## 🚀 Features

- **Dropout Prediction**: Predicts verification/risk of student dropout based on academic and demographic factors.
- **REST API**: Fast and efficient API built with **FastAPI**.
- **Interactive UI**: User-friendly web interface built with **Streamlit**.
- **Containerized**: Fully Dockerized for consistent deployment across environments.
- **ML Integration**: Uses a pre-trained **LightGBM** model for high-accuracy predictions.

## 🛠️ Tech Stack

- **Language**: Python 3.10
- **Web Framework**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **Machine Learning**: LightGBM, Scikit-learn, NumPy, Pandas, Joblib
- **Containerization**: Docker
- **Data Format**: JSON

## 📂 Project Structure

```
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── schema.py        # Pydantic models for data validation
│   └── __init__.py
├── frontend/
│   └── streamlit_app.py # Streamlit frontend application
├── model/
│   └── student_attendance_trainned_model.pkl  # Trained LightGBM model
├── data/
│   └── student-mat.csv  # Dataset used for training/analysis
├── notebooks/
│   └── day1_data_understanding.ipynb # Data exploration notebook
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## ⚡ Setup & Installation

### Option 1: Running with Docker (Backend Only)

1.  **Build the Docker image:**
    ```bash
    docker build -t student-dropout-api .
    ```

2.  **Run the container:**
    ```bash
    docker run -p 8000:8000 student-dropout-api
    ```

The API will be available at `http://localhost:8000`.

### Option 2: Running Locally (Full System)

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Student-attendance
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the FastAPI Backend:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will run at `http://127.0.0.1:8000`.

5.  **Run the Streamlit Frontend:**
    Open a new terminal, activate the environment, and run:
    ```bash
    streamlit run frontend/streamlit_app.py
    ```
    The frontend will open in your browser at `http://localhost:8501`.

## 🔌 API Usage

### Health Check
- **URL**: `/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "message": "Student Dropout Prediction API is running"
  }
  ```

### Predict Dropout Risk
- **URL**: `/predict`
- **Method**: `POST`
- **Body** (JSON):
  ```json
  {
      "age": 18,
      "studytime": 2,
      "failures": 0,
      "absences": 4,
      "Medu": 4,
      "Fedu": 3,
      "internet": 1,
      "G1": 15,
      "G2": 16
  }
  ```
- **Response**:
  ```json
  {
      "dropout_risk": 0,
      "risk_probability": 0.12
  }
  ```
  *(Note: `dropout_risk` 0 means low risk, 1 means high risk)*

## 📊 Data & Model

- The model is trained on student performance data (including grades `G1`, `G2`, absences, etc.).
- It uses **LightGBM**, a gradient boosting framework that uses tree-based learning algorithms, known for its speed and efficiency.
