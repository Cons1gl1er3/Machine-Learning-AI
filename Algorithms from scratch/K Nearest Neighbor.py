import numpy as np
from collections import Counter

def distance(x1, x2):
    return np.sqrt(np.sum(x1 - x2)**2)

class KNN:
    def __init__(self, k):
        self.k = k
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    def label(self, x):
        distances = [distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
    def predict(self, X_valid):
        predicted_labels = [self.label(x_valid) for x_valid in X_valid]
        return np.array(predicted_labels)