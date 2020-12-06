import requests
import json
from flask import Response, Flask
import time
import csv



app = Flask(__name__)

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(5)
    return rv

@app.route('/')
# def render_large_template():
#     rows = iter_all_rows()
#     return Response(stream_template('index2.html', rows=rows))


def iter_all_rows():
    with open("stream.csv") as wfile:
        reader = csv.reader(wfile)
        for index,line in enumerate(reader):
            if index == 0:
                continue
            
            url = 'http://127.0.0.1:5000/results'
            data= [float(x) for x in line]

            r = requests.post(url,json={'Wellhead Temp. (C)':data[0], 'Wellhead Press (psi)':data[1], 'MMCFD- gas':data[2], 
            'BOPD (barrel of oil produced per day)': data[3],'BWPD (barrel of water produced per day)': data[4],
            'BSW - basic solid and water (%)': data[5],'CO2 mol. (%) @ 25 C & 1 Atm.': data[6], 'Gas Grav': data[7]})
            #print(round(r.json(),2))
            if (r.json() >= 0.25 and r.json() <= 1.6):  
                print("Severe Corrosion Defect:{} mm".format(round(r.json(),2)))
            elif (r.json() >= 0.13 and r.json() <= 0.249):
                print("High Corrosion Defect:{} mm".format(round(r.json(),2)))
            elif (r.json() >= 0.129 and r.json() <= 0.025):
                print("Mild Corrosion Defect:{} mm".format(round(r.json(),2)))
            else:
                print("Low Corrosion Defect:{} mm".format(round(r.json(),2)))
            time.sleep(10)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
