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


def get_estimated(age, sex, cp_0, cp_1, cp_2, cp_3, trestbps, chol, fbs, restecg_0, restecg_1, restecg_2, thalachh, exang_0, exang_1, oldpeak, slp_0, slp_1, slp_2, caa_0, caa_1, caa_2, caa_3, caa_4, thall_0, thall_1, thall_2, thall_3):
    dic = {
        'age': [age],
        'sex': [sex],
        'cp_0': [cp_0],
        'cp_1': [cp_1],
        'cp_2': [cp_2],
        'cp_3': [cp_3],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg_0': [restecg_0],
        'restecg_1': [restecg_1],
        'restecg_2': [restecg_2],
        'thalachh': [thalachh],
        'exang_0': [exang_0],
        'exang_1': [exang_1],
        'oldpeak': [oldpeak],
        'slp_0': [slp_0],
        'slp_1': [slp_1],
        'slp_2': [slp_2],
        'caa_0': [caa_0],
        'caa_1': [caa_1],
        'caa_2': [caa_2],
        'caa_3': [caa_3],
        'caa_4': [caa_4],
        'thall_0': [thall_0],
        'thall_1': [thall_1],
        'thall_2': [thall_2],
        'thall_3': [thall_3]
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
    age = request.form['age']
    sex = request.form['sex']
    cp_0 = request.form['cp_0']
    cp_1 = request.form['cp_1']
    cp_2 = request.form['cp_2']
    cp_3 = request.form['cp_3']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg_0 = request.form['restecg_0']
    restecg_1 = request.form['restecg_1']
    restecg_2 = request.form['restecg_2']
    thalachh = request.form['thalachh']
    exng_0 = request.form['exng_0']
    exng_1 = request.form['exng_1']
    oldpeak = request.form['oldpeak']
    slp_0 = request.form['slp_0']
    slp_1 = request.form['slp_1']
    slp_2 = request.form['slp_2']
    caa_0 = request.form['caa_0']
    caa_1 = request.form['caa_1']
    caa_2 = request.form['caa_2']
    caa_3 = request.form['caa_3']
    caa_4 = request.form['caa_4']
    thall_0 = request.form['thall_0']
    thall_1 = request.form['thall_1']
    thall_2 = request.form['thall_2']
    thall_3 = request.form['thall_3']

    response = jsonify({
        'estimated_value': int(get_estimated(age, sex, cp_0, cp_1, cp_2, cp_3, trestbps, chol, fbs, restecg_0, restecg_1, restecg_2, thalachh, exng_0, exng_1, oldpeak, slp_0, slp_1, slp_2, caa_0, caa_1, caa_2, caa_3, caa_4, thall_0, thall_1, thall_2, thall_3))
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    load_saved_artifacts()
    print('starting python flask server')
    app.run()
