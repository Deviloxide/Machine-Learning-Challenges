import numpy as np
def linear_regression_normal_equation(X, y):
    # theta = (X^T * X)^-1 * X^T * y
    X_Transposed = np.transpose(X)
    inverse_term = np.linalg.inv(np.matmul(X_Transposed, X))
    result = np.matmul(np.matmul(inverse_term, X_Transposed), y)
    rounded_result = np.round(result, decimals=2)
    return rounded_result.tolist()

print(linear_regression_normal_equation([[1, 2], [1, 3], [5, 3]], [1, 2, 3]))