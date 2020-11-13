# import relevant packages
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from faker import Faker

# initialize faker
fake = Faker()
# Detecting external corrosion

df1 = pd.read_csv('data.csv', sep=',')
# print(df1.columns)
print(df1.describe().T)

np.random.seed(42)
df2 = pd.DataFrame({"Wellhead Temp. (C)":np.random.uniform(41.07, 73.87,5000), 
                    "Wellhead Press (psi)":np.random.uniform(382.08, 2317.23, 5000),
                    "MMCFD- gas":np.random.uniform(0.23, 17.54, 5000),
                    "BOPD (barrel of oil produced per day)":np.random.uniform(129.47, 2087.43, 5000),
                    "BWPD (barrel of water produced per day)":np.random.uniform(40.61, 9314.26, 5000),
                    "BSW - basic solid and water (%)":np.random.uniform(0.13, 89.26, 5000),
                    "CO2 mol. (%) @ 25 C & 1 Atm.":np.random.uniform(0.6786, 4.2983, 5000),
                    "Gas Grav.":np.random.uniform(0.7111, 0.9319, 5000),
                    "CR-corrosion defect":np.random.uniform(0.0009, 0.4052, 5000)}) 

df2.to_csv('fake_data.csv')
df2 = pd.read_csv('fake_data.csv', sep=',')
print(df2.describe().T)