from flask import Flask
import numpy
import json
import sys
import pandas

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

import sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def test():
    return 'testing...'

filename = 'trained_model.sav'

@app.route('api/v0/test'), methods= ['GET', 'POST']
def predict_test():
    request = pd.DataFrame([request.json])
    loaded_model = joblib.load(filename)
    res = str(loaded_model.predict())