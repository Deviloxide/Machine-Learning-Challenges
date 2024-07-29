import TransposeMatrix as TM

def calculate_matrix_mean(matrix, mode):
    means = []
    if mode == 'column':
        matrix = TM.transpose_matrix(matrix)
    for row in matrix:
        means.append(sum(row) / len(row))
    return means
