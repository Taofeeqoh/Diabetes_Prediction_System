from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

#load the model
model = pickle.load(open("model.pkl", "rb"))["model_name"]
scaler = pickle.load(open("scaler.pkl", "rb"))


@app.route("/", methods=["GET"])
def hello_world():
    prediction = ''
    return render_template('index.html', prediction=prediction)

@app.route("/predict", methods=["POST"])
def predict():
    pregnancies = int(request.form["pregnancies"])
    glucose = int(request.form["glucose"])
    blood_pressure = int(request.form["blood_pressure"])
    skin_thickness = int(request.form["skin_thickness"])
    insulin = int(request.form["insulin"])
    bmi = float(request.form["bmi"])
    diabetes_pedigree = float(request.form["diabetes_pedigree"])
    age = int(request.form["age"])
    
    variables = np.asarray([pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree,age]).reshape(1,-1)
    
    transformed = scaler.transform(variables)
    outcome = model.predict(transformed)[0]
    if outcome == 1:
        prediction = "Based on the provided information, our analysis suggests a high likelihood of diabetes. We strongly recommend consulting a healthcare professional for further diagnosis and personalized medical guidance."
    else:
        prediction = "Based on the provided information, our analysis does not indicate a high risk of diabetes. However, we encourage maintaining a healthy lifestyle and regular check-ups for overall well-being."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(port=3000,debug=True)