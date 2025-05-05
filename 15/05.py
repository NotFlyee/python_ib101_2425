def triangle(a, b, c):
    temp = sorted([a, b ,c])
    print('Это треугольник' if sum(temp[:-1]) > max(temp) else 'Это не треугольник')

