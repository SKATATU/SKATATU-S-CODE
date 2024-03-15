from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import json

app = Flask('app')
CORS(app)

def get_database():
  SHEET_ID = '1zCb3iblqd-xg31OlPezRyf_LlEEKR8w2OPQ2WWFa3jc'
  SHEET_NAME = 'Sheet1'
  url = 'https://docs.google.com/spreadsheets/d/'+SHEET_ID+'/gviz/tq?tqx=out:csv&sheet='+SHEET_NAME
  df = pd.read_csv(url)
  return df.to_json(orient='records') #convert to json string

@app.route('/test', methods=['GET'])
def test():
  data_json=get_database()
  getName = request.values.get('inpname')
  data = json.loads(data_json) #convert to a list of json objects
  for i in range(len(data)):
    if data[i]['Name']==getName:
      return str(data[i]['Clno'])
  return data

@app.route('/all', methods=['GET'])
def getAll():
  data_json=get_database() #a json string is received
  return data_json

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
