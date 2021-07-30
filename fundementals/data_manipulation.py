from __future__ import division
import numpy as np
import math
import sys
from itertools import combinations_with_replacement


def shuffle_data(X: np.array, y: np.array, seed=None):
    """Random shuffling of samples in X and y"""

    if seed:
        np.random.seed(seed)

    # get shuffled indices
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)

    return X[idx], y[idx]


def train_test_split(X, y, test_size=0.5, shuffle=True, seed=None):
    """Split the data into train and test sets"""
    if shuffle:
        X, y = shuffle_data(X, y, seed)

    # split the training data from test data in the ratio specified in test_size
    split_i = len(y) - int(len(y) // (1 / test_size))
    
    X_train, X_test = X[:split_i], X[split_i:]
    y_train, y_test = y[:split_i], y[split_i:]

    return X_train, X_test, y_train, y_test

