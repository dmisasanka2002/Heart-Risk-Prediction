# **🫀 Heart Risk Prediction Web App**

This is a simple yet powerful heart disease risk prediction system built using Python, Scikit-learn, and Flask. The app predicts a numerical risk score for heart disease based on patient lifestyle and medical history.

## **🔍 Project Overview**

The main objective of this project is to provide a basic regression-based heart risk prediction using machine learning. The model is trained using real-world health-related features, allowing users to estimate their risk level based on individual inputs.

## 📊 Features Used

- Sex (male/female)
- Age
- Total Cholesterol (TC)
- HDL Cholesterol (HDL)
- Smoking status (smoking / no smoking)
- Blood Pressure Medication (yes / no)
- Diabetes (yes / no)

## 🧪 ML Pipeline

- Preprocessing:
  - Handling missing values
  - Feature scaling
  - Categorical encoding
- Model: GradientBoostingRegressor
- Validation: Cross-validation & Hyperparameter tuning using GridSearchCV

## 🖥️ Flask Web App

A simple UI that allows users to:
- Input personal and medical data
- Get a real-time heart disease risk score
- Visualize prediction instantly

> Currently hosted locally via Flask.

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/dmisasanka2002/Heart-Risk-Prediction.git
   cd Heart-Risk-Prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```bash
   python app/main.py
   ```

## 📁 Folder Structure

```bash
📦Heart Risk Prediction
 
 ┣ 📂app/ # Flask application
 ┣ 📂data/ # Data and data models
 ┣ 📂models/ # ML pipeline and saved model
 ┣ 📂notebooks/
 ┣ 📜README.md
 ┗ 📜requirements.txt
```

---