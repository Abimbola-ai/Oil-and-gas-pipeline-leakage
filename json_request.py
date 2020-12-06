import requests
import json
from flask import Response, Flask
import time


app = Flask(__name__)


url = 'http://127.0.0.1:5000/results'

r = requests.post(url,json={'Wellhead Temp. (C)':53.35, 'Wellhead Press (psi)':1105.13, 'MMCFD- gas':12.87, 
    'BOPD (barrel of oil produced per day)': 1378.93,'BWPD (barrel of water produced per day)': 2812.62,
    'BSW - basic solid and water (%)': 75.64,'CO2 mol. (%) @ 25 C & 1 Atm.': 3.3628, 'Gas Grav': 0.7205})

print(r.json())
