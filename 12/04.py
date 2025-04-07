print(' '.join(str(i ** 2) for i in [int(i) for i in input().split()] if i % 2 and i ** 2 % 10 != 9))
