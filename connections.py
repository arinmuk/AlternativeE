import sys
import pandas as pd
from sqlalchemy.dialects.mssql import pymssql
from sqlalchemy import create_engine, MetaData, Table, select
import sqlalchemy

import pymongo
import csv
import json
from config import cloudM,cloudMpassword,sqluser,sqlpass,servername
from pymongo import MongoClient
from flask import Flask, jsonify, render_template


#local mongo install



#cloud mongo connect
cloudMClnt=MongoClient()
cloudMClnt=MongoClient("mongodb+srv://"+ cloudM + ":"
                       + cloudMpassword + "@cluster0-omshy.mongodb.net/test?retryWrites=true&w=majority")




from sqlalchemy import create_engine, MetaData, Table, select






# read cloud Mongo Data and return dataframes
def cloudM_R():
  db=cloudMClnt['AlternativeE']
  coldata=db['data']
    
  Adatadf = pd.DataFrame(list(coldata.find().sort([('ID', 1)])))
  del Adatadf['_id']
  return Adatadf


#insert data into local mongo


