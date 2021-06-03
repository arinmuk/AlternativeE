from flask import Flask,render_template,jsonify,request
import json
from flask_cors import CORS, cross_origin

from pymongo import MongoClient 
from connections import cloudM_R
import os 

port = int(os.environ.get('PORT', 5000)) 
#app.run(host='0.0.0.0', port=port)


app=Flask(__name__)
CORS(app, support_credentials=True)






@app.route("/")
@cross_origin(supports_credentials=True)
def home():

    
    return render_template('index.html')

@app.route("/readData")
@cross_origin(supports_credentials=True)
def read():
        altdatadf = cloudM_R()
        resdf=altdatadf[(altdatadf["Year"]==2019)]
        return jsonify(resdf.to_dict('records'))







#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if __name__=='__main__':
    #app.run(host='0.0.0.0', port=port)
    app.run(debug=True)