import requests
import json
from flask import Response, Flask,render_template
import time
import csv, os
import pandas as pd
import flask




app = flask.Flask(__name__)
last = -1

@app.route('/')
def render():
    return flask.render_template('index2.html')

@app.route('/pred')
def iter_all_rows():
    global last
    with open("stream.csv") as wfile:
        reader = csv.reader(wfile)
        for row_no,row in enumerate(reader):
            num = row[0]

            if row_no <= last:
                continue   

            url = 'http://127.0.0.1:5000/results'
        
            r = requests.post(url,json={'Wellhead Temp. (C)':row[0], 'Wellhead Press (psi)':row[1], 'MMCFD- gas':row[2], 
            'BOPD (barrel of oil produced per day)': row[3],'BWPD (barrel of water produced per day)': row[4],
            'BSW - basic solid and water (%)': row[5],'CO2 mol. (%) @ 25 C & 1 Atm.': row[6], 'Gas Grav': row[7]})
         
            last = row_no
           
            return {'WellheadTemp':row[0], 'WellheadPressure':row[1], 'MMCFDgas':row[2], 
            "BOPD": row[3],'BWPD': row[4],
            'BSW': row[5],"CO2": row[6], 'GasGrav': row[7],"predicted": round(r.json(),2)}
            
            time.sleep(10)
                  

if __name__ == '__main__':
    app.run(debug=True, port=5001)


