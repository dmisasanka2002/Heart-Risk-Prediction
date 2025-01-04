from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

model = joblib.load('models/model.pkl')
preprocesser = joblib.load('models/preprocesser.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getresults', methods=['POST'])
def getresults():
    gender_dict = {'female': 0, 'male': 1}
    
    result = request.form
    
    name = result['name']
    gender = result['gender']
    age = float(result['age'])
    tc = float(result['tc'])
    hdl = float(result['hdl'])
    smoke = int(result['smoke'])
    bpmed = int(result['bpmed'])
    diab = int(result['diab'])
    
    test_data = np.array([gender_dict[gender], age, tc, hdl, smoke, bpmed, diab]).reshape(1, 7)

    # Column names
    columns = ['SEX', 'AGE', 'TC', 'HDL', 'SMOKE_', 'BPMED', 'DIAB_noyes']

    # Create DataFrame
    df = pd.DataFrame(test_data, columns=columns)
    num_cols = ['AGE', 'TC', 'HDL']
    df[num_cols] = preprocesser.transform(df)

    prediction = model.predict(df)
    
    resultDict = {"name": name, "risk": round(prediction[0] * 100, 2)}
    
    return render_template('patient_results.html', results=resultDict)

if __name__ == '__main__':
    app.run(debug=True)
