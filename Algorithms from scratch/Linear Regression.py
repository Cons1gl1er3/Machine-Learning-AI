import numpy as np

class LinearRegression:
    def __init__(self):
        pass
    
    def fit(self, X_train, y_train):
        X_train = np.concatenate((X_train, np.ones((X_train.shape[0], 1))), axis = 1)
        w = np.linalg.pinv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)
        self.w = w
    
    def predict(self, X_valid):
        X_valid = np.concatenate((X_valid, np.ones((X_valid.shape[0], 1))), axis = 1)
        return X_valid.dot(self.w)