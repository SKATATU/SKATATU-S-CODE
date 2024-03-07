from flask import Flask, request
from flask_cors import CORS

app = Flask('app')
CORS(app)

data = [
    {"id": "1", "name": "John"},
    {"id": "2", "name": "Peter"},
    {"id": "3", "name": "Mary"}
]

@app.route('/getname', methods=['GET'])

def getName():
    name = request.values.get('id')
    for i in range(0,len(data)):
      if data[i]['id'] == name:
        return data[i]["name"]
    return "None"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
