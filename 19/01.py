def matrix(n=1, m=0, a=0):
    if m == 0:
        return [[a] * n] * n
    return [[a] * m] * n
