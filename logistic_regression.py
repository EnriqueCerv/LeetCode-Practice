# %%
import pandas as pd
import numpy as np
import sklearn
# %%
# Assumese we have a csv file from which to get the data
file = 'social_network_ads.csv'

# Downloading data
df = pd.read_csv(file, index_col=False, header=0)
df

# Dividing into features and target
X = df.iloc[:,2:-1]
y  = df.iloc[:,-1]
X,y

# Dividing into train, test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

# Standardizing data, not stricly necessary but sometimes does better
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)


# %%
# Building the model
model = sklearn.linear_model.LogisticRegression()
model.fit(X_train, y_train)

# Testing the model
y_pred = model.predict(X_test)
from sklearn.metrics import accuracy_score, classification_report
score = accuracy_score(y_test, y_pred)
print(score, classification_report(y_test, y_pred))
# %%
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
reg = LogisticRegression()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25)

reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report

score = accuracy_score(y_test, y_pred)
print(score)
print(classification_report(y_test, y_pred))