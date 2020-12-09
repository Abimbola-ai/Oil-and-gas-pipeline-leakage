# Import necessary library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn import ensemble
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from math import sqrt
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.utils import resample
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve,roc_auc_score
from sklearn.metrics import confusion_matrix, f1_score,classification_report
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
from sklearn.multiclass import OneVsRestClassifier
from itertools import cycle
plt.style.use('ggplot')
import warnings
warnings.filterwarnings("ignore")
import pickle

data = pd.read_csv("generated_dataset.csv")
#data.head()

data['CRDC']=data['CR-corrosion defect']
data = data.rename(columns = {'CR-corrosion defect':"CRD"}, inplace=False)
#data.head()

data['CRDC'][(data.CRD<0.025)]= 'LOW(0.01 - 0.025 mm)'
data['CRDC'][(data.CRD>=0.025)&(data.CRD<0.13)]= 'MILD(0.0251 - 0.13 mm)'
data['CRDC'][(data.CRD>=0.013)&(data.CRD<0.25)]= 'HIGH(0.131 - 0.25 mm)'
data['CRDC'][(data.CRD>=0.250)]= 'SEVERE(0.251 - 1.57 mm)'
data = data.drop('CRD', axis=1)
#print(data.head())


data['CRDC']=data['CRDC'].astype('category')

# Split data into predictor and targets
y = data.CRDC
X = data.drop(['CRDC'],axis=1)
labels=list(X.columns)
number_features = len(labels)


# Split Data to test and train set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

decision = DecisionTreeClassifier()
decision.fit(X_train, y_train) # fit model

print('Accuracy: {}\n\n  Report:\n  {}'.format(decision.score(X_test, y_test),
      classification_report(y_test,decision.predict(X_test))))

# save the model to disk

pickle.dump(decision, open('digital_model_class.pkl', 'wb'))

# load the model from disk
model = pickle.load(open('digital_model_class.pkl', 'rb'))
print(model.predict([[53.35,1105.13,12.87,1378.93,2812.62,75.64,3.3628,0.7205]]))
