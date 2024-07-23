import numpy as np

def reshape_matrix(a, new_shape):
    reshaped_matrix = np.reshape(a, new_shape)
    return reshaped_matrix.tolist()