# Diabetes_Prediction_System Using Flask

This is a **Diabetes Prediction Web Application** built using **Flask**, **Scikit-Learn**, and **Machine Learning** models. The app predicts whether a user is likely to have diabetes based on medical data such as **Glucose levels**, **BMI**, **Blood Pressure**, and more. The prediction is made using a pre-trained **machine learning model** (e.g., SVC - Support Vector Classifier).

---

## Project Overview

This web application uses **Flask** to create an interface where users can input personal health data such as:
- Number of Pregnancies
- Glucose level
- Blood Pressure
- Skin Thickness
- Insulin level
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

Once the user submits the data, the app processes the information and predicts the likelihood of diabetes using a pre-trained **machine learning model**. The results are shown on the web page with personalized guidance.

---

## Features

- **User-friendly interface** for easy input of health data.
- **Diabetes prediction** using machine learning.
- **Flask-based web app** that serves the prediction.
- **Model retraining**: You can retrain the model with new data.
- **Data Preprocessing** using **StandardScaler**.


## Model Details

This application uses the **Support Vector Classifier (SVC)** for diabetes prediction. The model is trained using **Scikit-Learn** with health data as features and diabetes status (0 = No, 1 = Yes) as the target variable.

- The **dataset** used for training the model is derived from the Pima Indians Diabetes Database.
- The model was saved using **Pickle** to make it accessible in the Flask app.
- The data is scaled using **StandardScaler** for better model performance.
