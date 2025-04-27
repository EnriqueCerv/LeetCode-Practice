# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, classification_report
# %%
# The linear regression first

# Make up data

rng = np.random.RandomState(0)
n_samples, n_features = 500, 20

cov = np.random.randint(2,5, size=(n_features, n_features))
X = rng.multivariate_normal(mean = [0]*n_features, cov=cov, size=n_samples)

# plt.scatter(X[:,0],X[:,1])

# Now for the real data: y = Xw + eps
w = np.random.normal(loc = 1, scale = 2, size=n_features)
eps = np.random.randn(n_samples)

y_true = np.dot(X, w) + eps

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y_true, test_size=0.25)
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_pred = lin_reg.predict(X_test)

mse, r2 = mean_squared_error(y_test, y_pred), r2_score(y_test, y_pred)
mse, r2
# %%
# The logistic regression

# Import data
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)

acc, class_rep = accuracy_score(y_test, y_pred), classification_report(y_test, y_pred)
acc, class_rep
# %%
# Logistic regression with pandas

df = pd.read_csv('social_network_ads.csv',  index_col = False, header = 0)
df

X = df.iloc[:,2:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)

acc, class_rep = accuracy_score(y_test, y_pred), classification_report(y_test, y_pred)
acc, class_rep