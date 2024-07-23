def scalar_multiply(matrix, scalar):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = [[0] * num_cols for row in range(num_rows)]
    for row in range(num_rows):
        for col in range(num_cols):
            result[row][col] = matrix[row][col] * scalar
    return result