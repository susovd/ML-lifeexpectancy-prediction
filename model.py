import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats import linregress
import pickle
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#import data
df = pd.read_csv("demographics_data.csv")


#birth, fertility and TB
#set up test and train columns
# load the dataset
data = df.values
X, y = data[:, :-1], data[:, -1]


#splitting the dataset into training and test set
X_train, X_test, y_train, y_test=train_test_split(X, y, random_state=42, test_size=0.15)

# with new parameters
gbr = GradientBoostingRegressor(n_estimators=600, max_depth=5, learning_rate=0.01, min_samples_split=3)

#fit the model
gbr.fit(X_train, y_train)

#save the model to disk
pickle.dump(gbr, open('model.pkl', 'wb'))

#predicting  the test set result
y_pred = gbr.predict(X_test)

#get MSE
#mse = mean_squared_error(y_test,ypred)
#print("MSE: %.2f" % mse)

# define new test data to validate this program
row = [81,9,17,24.6,24.3]

#loading model to comapre the results
model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([row]))
