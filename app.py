import numpy as np
import pandas as pd
import gmaps
import gmaps.datasets
from flask import Flask, request, render_template


# #key from Env var
# gmaps.configure(api_key=os.environ["GOOGLE_API_KEY"])
#
# crime=pd.read_csv("Boston_crime_incidents.csv")
#
# print(crime.head())




app = Flask(__name__)

@app.route('/')
def frontpage():
    return  render_template('index.html')

@app.route('/', methods=['POST'])
def frontpage_post():
    min_temp = request.form['min_temp']
    max_temp = request.form['min_temp']
    price = request.form['min_temp']
    year = request.form['min_temp']
    return render_template('results.html', min_temp = min_temp, max_temp = max_temp, price = price, year = year)

if __name__ == "__main__":
    app.run()
