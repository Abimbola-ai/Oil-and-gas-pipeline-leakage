# import relevant packages
import pandas as pd
import numpy as np


np.random.seed(42)
df2 = pd.DataFrame({"External Temperature (DegC)":np.random.uniform(21.4, 32.8,8000), 
                    "Humidity(%)":np.random.uniform(80.0, 90.0, 8000),
                    "Wellhead Temp. (C)":np.random.uniform(41.07, 73.87,8000), 
                    "Wellhead Press (psi)":np.random.uniform(382.08, 2317.23, 8000),
                    "BOPD (barrel of oil produced per day)":np.random.uniform(129.47, 2087.43, 8000),
                    "BWPD (barrel of water produced per day)":np.random.uniform(40.61, 9314.26, 8000),
                    "BSW - basic solid and water (%)":np.random.uniform(0.13, 89.26, 8000),
                    "CO2 mol. (%) @ 25 C & 1 Atm.":np.random.uniform(0.6786, 4.2983, 8000),
                    "Gas Grav.":np.random.uniform(0.7111, 0.9319, 8000),
                    "Pipe wall thickness (mm)":np.random.uniform(24, 4, 8000)}) 

print(df2.head())
# Create new column for a set of conditions
# df2['External corrosion'] = np.where((df2["Pipe wall thickness (mm)"] >= 24.0) & (df2["Pipe wall thickness (mm)"] <= 21.0), "Good")
def label_corrosion(row):
    if (row["Pipe wall thickness (mm)"] >= 24.0) and (row["Pipe wall thickness (mm)"] <= 21.0):  
        return 'Good'
    elif (20.0 <= row["Pipe wall thickness (mm)"] >= 16.0):
        return 'Minor'
    elif 15.0 <= row["Pipe wall thickness (mm)"] >= 11.0:
        return 'Medium'
    else:
        return 'Severe'
df2['External Corrosion'] = df2.apply(lambda row: label_corrosion(row), axis=1)

df2.to_csv('fake_data_thickness.csv')
df2 = pd.read_csv('fake_data_thickness.csv', sep=',')
print(df2.describe().T)