from random import sample
from pprint import pprint

def make_bingo() -> tuple[tuple]:
    temp = list()
    values = sample(range(1, 76), 25)
    for i in range(0, 25, 5):
        temp.append(values[i:i + 5])
    temp[2][2] = 0
    return tuple(map(lambda x: tuple(x), temp))

res = make_bingo()
pprint(res)
