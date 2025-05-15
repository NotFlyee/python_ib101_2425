def swap(first: list[int], second: list[int]):
    first[:], second[:] = second[:], first[:]
