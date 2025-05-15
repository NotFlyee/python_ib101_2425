def transpose(matrix: list[list[int]]):
    temp = matrix[:]
    matrix.clear()
    for i in range(len(temp)):
        matrix += [[j[i] for j in temp]]
