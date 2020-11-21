# Import necessary library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pickle

from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn import ensemble
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from math import sqrt


# Import data
data = pd.read_csv('generated_dataset.csv')
data.head()

# Data Modelling
X = data.iloc[:,0:8].values
y = data.iloc[:,8]
#X = MinMaxScaler().fit_transform(X)

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape,X_test.shape)

# Run a Gradient Boost Model
gbm_model = ensemble.GradientBoostingRegressor(n_estimators=15000, max_depth=4, min_samples_leaf=15, 
                                           min_samples_split=10, learning_rate=0.01, loss='huber', random_state=5)

# Reshape train_target to be a 1d array
#y_train = y_train.as_matrix().flatten()

# Fit model
gbm_model.fit(X_train, y_train)

# Make predictions with model
y_pred = gbm_model.predict(X_test)

#Score the model
# print("Score:", gbm_model.score(X_test, y_test))
# print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
# print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
# print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# save the model to disk

pickle.dump(gbm_model, open('digital_model.pkl', 'wb'))

# load the model from disk
model = pickle.load(open('digital_model.pkl', 'rb'))
print(model.predict([[53.35,1105.13,12.87,1378.93,2812.62,75.64,3.3628,0.7205]]))
# result = loaded_model.score(X_test, y_test)
# print(result)