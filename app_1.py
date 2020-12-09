from flask import Flask, request, jsonify, render_template
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
#from digitalModel import loaded_model

app = Flask(__name__)
model = pickle.load(open('digital_model_class.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)  
    #output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='CR - Corrosion Defect is {}'.format(prediction))
    
@app.route('/results',methods=['POST'])
def results():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    result = jsonify(output)
    return result


if __name__ == '__main__':
    app.run(debug=True, port=5000)