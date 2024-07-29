import numpy as np


def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    for iteration in range(iterations):
        hypothesis = np.matmul(X, theta)
        loss = hypothesis - y.reshape(-1, 1)
        gradient = np.matmul(X.T, loss) / m
        theta -= alpha * gradient
    result = np.round(theta, decimals=4)
    flattened_result = result.flatten()

    return flattened_result
