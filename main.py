from flask import Flask, jsonify, request
import pandas as pd
df = pd.read_csv('calculated copy.csv')
app = Flask(__name__)


Radius = df["Radius"].tolist()
Mass = df["Mass"].tolist()
Gravity = df["Gravity"].tolist()
Distance = df["Distance"].tolist()
StarName = df["Star Name"].tolist()
data = [
    {'mass': Mass},
    {'radius': Radius},
    {'gravity': Gravity},
    {'distance': Distance},
    {'starName': StarName}
]


@app.route('/reachData')
def getData():
    return jsonify({
        'data': data 
    })

if (__name__ == '__main__'):
    app.run(debug=True)