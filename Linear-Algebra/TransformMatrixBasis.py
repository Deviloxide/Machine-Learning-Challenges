import numpy as np

def transform_basis(B, C):
    C_Inverse = np.linalg.inv(C)
    result = np.matmul(B, C_Inverse)
    rounded_result = np.round(result, decimals=4)
    return rounded_result.tolist()
