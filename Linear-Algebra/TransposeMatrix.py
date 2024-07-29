def transpose_matrix(a):
    unpacked_lists = zip(*a)
    a = [list(i) for i in unpacked_lists]
    return a
