import numpy as np

def snake(rows: int, cols: int):
    matrix = np.arange(1, rows * cols + 1).reshape(rows, cols)
    matrix[::2] = matrix[::2, ::-1]
    return matrix
