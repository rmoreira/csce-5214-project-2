#!/usr/bin/env python
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, Markup
from sklearn.linear_model import LinearRegression
import pickle

# load linear regression model
model = pickle.load(open('model.sav', 'rb'))

# load model's features
features = pickle.load(open('features.sav', 'rb'))
 
app = Flask(__name__)
 
@app.route("/", methods=['POST', 'GET'])
def index():
    # on load set form with defaults
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    # create an empty list that stores user's inputs
    user_inputs = [[]]

    for feature in features:
        if request.method == 'POST':    # form submission
            user_inputs[0].append(float(request.form[feature]))
        else:                           # get request
            user_inputs[0].append(float(request.args.get(feature)))
    
    pred_price = model.predict(user_inputs)[0]   # model's prediction
    return redirect(url_for('success', price=pred_price))

@app.route('/success/<price>')
def success(price):
   return price

# when running app locally
if __name__=='__main__':
      app.run(debug=True)