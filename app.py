from distutils.log import debug
from pyexpat import model
import numpy as np
from flask import Flask,request,jsonify,render_template

import pickle

app=Flask(__name__)

model=pickle.load(open("pickel_model.pkl","rb"))

@app.route("/predict",method_=_["POST"])

def predict():
    json_=request.json
    query_df=pd.DataFrame(json_)
    prediction=model.predict(query_df)
    return jsonify({"prediction":list(prediction)})

if __name__=="__main__":
    app.run(debug=True)    