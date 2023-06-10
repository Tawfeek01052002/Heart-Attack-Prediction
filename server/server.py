from flask import Flask , request , jsonify
import util


app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
	response = jsonify({
		'locations' : util.get_location_names()
		})
	response.headers.add('Access-Control-Allow-Origin' , '*')

	return response
		
@app.route('/predict_value',methods = ['GET','POST'])
def predict_value():
	

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
    	'estimated_value':int(util.get_estimated(age , sex , cp , trestbps , chol , fbs ,restecg , thalach , 
                 exang , oldpeak , slope , ca , thal))
    	})




    response.headers.add('Access-Control-Allow-Origin' , '*')
    return response

if __name__ == '__main__':
	print('starting python flask server')
	util.load_saved_artifacts()
	app.run(debug = True)



