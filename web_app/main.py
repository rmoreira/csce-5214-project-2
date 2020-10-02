#!/usr/bin/env python
from flask import Flask, render_template, flash, request, jsonify, Markup
from sklearn.linear_model import LinearRegression
import pickle

# load saved model
model = pickle.load(open('model.sav', 'rb'))

# load model's features
features = pickle.load(open('features.sav', 'rb'))
 
app = Flask(__name__)
 
@app.route("/", methods=['POST', 'GET'])
def index():
    # on load set form with defaults
    return render_template('index.html',
            model_intercept = model.intercept_,
            model_coef = list(model.coef_),
            features = features)


# when running app locally
if __name__=='__main__':
      app.run(debug=True)