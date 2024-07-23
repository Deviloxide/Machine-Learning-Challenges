def matrix_dot_vector(a, b):
    if len(a[0]) != len(b):
        return -1
    num_cols = len(a)
    num_rows = len(b)
    result = [0] * num_cols
    for row in range(num_cols):
        for col in range(num_rows):
            result[row] += a[row][col] * b[col]
    return result
