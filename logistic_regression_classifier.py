# %%
import pandas as pd
import numpy as np
import sklearn
# %%
from sklearn.datasets import load_iris
iris = load_iris()

# Make a data frame from the iris data set with titles iris.feature_names
df = pd.DataFrame(data = iris.data, columns = iris.feature_names)
# Add additional column with the target flower specie
df['species'] = iris.target_names[iris.target]
# Returns the top of the data frame
df.head()
# %%
# Here we prepare the data

# Independent variables are the features
X = df.iloc[:,:-1]
# Dependent variables are the targets
y = df.iloc[:,-1]

X, y

# Divide data into training and testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 1)

#%%
# Do the training
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

from sklearn.model_selection import GridSearchCV
parameter={'penalty':['l1','l2','elasticnet'],'C':[1,2,3,4,5,6,10,20,30,40,50],'max_iter':[100,200,300]}

classifier = GridSearchCV(model, param_grid=parameter, scoring='accuracy')

classifier.fit(X_train, y_train)
# %%
print(classifier.best_params_, classifier.best_score_)
# %%
# Onto the testing
y_pred = classifier.predict(X_test)

# Getting accuracy score
from sklearn.metrics import accuracy_score, classification_report
score = accuracy_score(y_test, y_pred)
print(score, classification_report(y_test, y_pred))