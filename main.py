from flask import Flask, request, jsonify
import json
import pickle
import numpy as np
import pandas as pd
from sklearn.compose import make_column_transformer

app = Flask(__name__)

__locations = None
__data_columns = None
__model = None

def get_estimated(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    dic = {
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    }
    data = pd.DataFrame(dic)
    return __model.predict(data)[0]

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading stats here...")
    global __locations
    global __data_columns
    global __model

    with open('./artifacts/column.json', 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    with open('./artifacts/heart_detail.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading is done...')

@app.route('/get_location_names')
def get_location_names_route():
    response = jsonify({
        'locations': get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_value', methods=['POST'])
def predict_value():
    load_saved_artifacts()
    age = request.form['ageui']
    sex = request.form['sex']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg = request.form['restecg']
    thalach = request.form['thalach']
    exang = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca = request.form['ca']
    thal = request.form['thal']

    response = jsonify({
        'estimated_value': int(get_estimated(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal))
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    load_saved_artifacts()
    print('starting python flask server')
    app.run()
