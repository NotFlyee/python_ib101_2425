def triangle(a, b, c):
    temp = sorted([a, b ,c])
    print('Это треугольник' if sum(temp[:-1]) > max(temp) else 'Это не треугольник')


triangle(1, 1, 2)
triangle(7, 6, 10)
