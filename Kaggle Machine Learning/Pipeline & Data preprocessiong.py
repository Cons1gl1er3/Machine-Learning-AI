import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score

data = pd.read_csv(r"D:\Coding\Mini Project\train.csv", index_col=0)
#print(data.head(5))

data.dropna(subset=['SalePrice'], inplace = True)
y = data.SalePrice
data.drop(columns='SalePrice', axis = 1, inplace = True)
numerical_cols = [col for col in data.columns if data[col].dtypes in ['int64', 'float64']]
object_cols = [col for col in data.columns if data[col].dtypes == 'object' and data[col].nunique() < 10]
X = data[numerical_cols+object_cols]

test = pd.read_csv(r'D:\Coding\Mini Project\test.csv', index_col=0)
y_test_train = test[numerical_cols+object_cols]

'''
numerical_prep = SimpleImputer()
categorical_prep = Pipeline(steps = [
    ('impute', SimpleImputer(strategy='most_frequent')), 
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Bundle together the preprocessing steps
preprocessor = ColumnTransformer(transformers = [
    ('numerical', numerical_prep, numerical_cols),
    ('categorical', categorical_prep, object_cols)
])

# Select model
model = RandomForestRegressor(n_estimators=100)

# Bundle together preprocess and model
my_pipeline = Pipeline(steps=[
    ("preprocessing", preprocessor),
    ("training", model)
])
'''
count = 1

def Try(train_size, numerical_strategy, n_estimators):
    global count
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=train_size)
    numerical_prep = SimpleImputer(strategy=numerical_strategy)
    categorical_prep = Pipeline(steps = [
        ('impute', SimpleImputer(strategy='most_frequent')), 
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    preprocessor = ColumnTransformer(transformers = [
        ('numerical', numerical_prep, numerical_cols),
        ('categorical', categorical_prep, object_cols)
    ])
    model = RandomForestRegressor(n_estimators=n_estimators)
    my_pipeline = Pipeline(steps=[
        ("preprocessing", preprocessor),
        ("training", model)
    ])
    scores = -1 * cross_val_score(my_pipeline, X, y, cv=5, scoring='neg_mean_absolute_error')
    final_score = scores.mean()
    plt.plot(count, final_score, 'ro')
    count+=1

Try(0.8, 'mean', 150)
plt.show()