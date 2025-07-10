import numpy as np


def generation(line: str) -> str:
    RULES = {'100', '010', '001', '011'}
    arr = np.array(list(line[-1] + line + line[0]))
    def next_gen(arr: np.ndarray, gen: int) -> str:
        new_arr = np.zeros(len(arr), dtype='U1')
        if gen == 10:
            return ''.join(arr[1:-1])
        for i in range(1, len(arr) - 1):
            comb = arr[i - 1] + arr[i] + arr[i + 1]
            new_arr[i] = '1' if comb in RULES else '0'
        new_arr[0], new_arr[-1] = new_arr[-2], new_arr[1]
        return next_gen(new_arr, gen + 1)

    return next_gen(arr, 1)
