from flask import Flask, render_template, request

import requests
from joblib import dump,load

import numpy as np

app = Flask(__name__)

model=load('Dragon.joblib')

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        f1 = float(request.form['f1'])
        f2=float(request.form['f2'])
        f3=float(request.form['f3'])
        f4=float(request.form['f4'])
        f5=float(request.form['f5'])
        f6=float(request.form['f6'])
        f7=float(request.form['f7'])
        f8=float(request.form['f8'])
        f9=float(request.form['f9'])
        f10=float(request.form['f10'])
        f11=float(request.form['f11'])
        f12=float(request.form['f12'])
        f13=float(request.form['f13'])
        # convert all f in 2d array
        new_prediction = model.predict(np.array([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13]]))
        return render_template('index.html',prediction_text="You Can Sell The House at {}".format(new_prediction[0]))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)