# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

from sklearn.preprocessing import StandardScaler
# %%
# Read data from a file:

file_path = 'file.csv'
df = pd.read_csv(file_path, header=0, index_col=False)
# %%
# Fill in missing values

df.interpolate(method = 'linear', inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)


# %%
# Create new features if needs be

df['new_feature'] = df['feature_1'] + df['feature_2']

# %%
# Normalise everything
scaler = StandardScaler()
numerical_cols = ['num_col1', 'num_col2']

for col in numerical_cols:
    df[col] = scaler.fit_transform(df[col])


# %%
# Get data
X = df.drop['target_column']
y = df['target_column']

X_train, X_test, y_train, y_test = train_test_split(X, y)
# %%
# Train model
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# %%
# Test model
y_pred = lin_reg.predict(X_test)

mse, r2 = mean_squared_error(y_test, y_pred), r2_score(y_test, y_pred)