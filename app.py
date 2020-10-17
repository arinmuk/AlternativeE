from flask import Flask,render_template,jsonify,request
import json
from pymongo import MongoClient 
from connections import cloudM_R


app=Flask(__name__)







@app.route("/")
def home():

    
    return render_template('index.html')

@app.route("/readData")
def read():
        altdatadf = cloudM_R()
        resdf=altdatadf[(altdatadf["Year"]==2019)]
        return jsonify(resdf.to_dict('records'))







#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if __name__=='__main__':
    app.run(debug=True)