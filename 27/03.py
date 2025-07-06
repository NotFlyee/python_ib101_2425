import numpy as np


def super_sort(rows: int, cols: int):
    arr_A = np.random.randint(1, 101, (rows, cols), dtype=np.uint8)
    arr_B = np.copy(arr_A)
    arr_B[:, 1::2].sort(axis=0)
    arr_B[:, ::2][::-1].sort(axis=0)
    return arr_A, arr_B
