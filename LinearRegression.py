# %%
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
# %%
# Create the random data
rng = np.random.RandomState(0)
n_samples, n_features = 500, 20
cov = np.random.randint(1,5, size=(n_features, n_features))
X = rng.multivariate_normal(mean=[0]*n_features, cov=cov, size=n_samples)

plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
# %%
# Figuring out what the true y's are: Usually y = Xw + eps
# Getting random weights

mu = 1
sigma = 2
w = np.random.normal(mu,sigma,size=(n_features))

epsilon = np.random.randn(n_samples)

y = np.dot(X, w) + epsilon


# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Train the model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Make predictions to test
y_pred = reg.predict(X_test)

# %%

from sklearn.metrics import mean_absolute_error, r2_score, classification_report
error = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
# print(error, classification_report(y_test, y_pred))
error, r2

# %%
# Can also do a PCA on the data

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X)

for i, (comp, var) in enumerate(zip(pca.components_, pca.explained_variance_)):
    comp = comp*var
    plt.plot([0,comp[0]], [0,comp[1]], label = f'Component {i}', color = f'C{i+2}', linewidth=3)

plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.plot()
# %%
