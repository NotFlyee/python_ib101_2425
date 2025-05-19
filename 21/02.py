data = []
for i in range(int(input())):
    n = int(input())
    data.append([int(input()[-1]) for j in range(n)])
print('ДА' if all([any(filter(lambda x: x % 5 == 0, i)) for i in data]) else 'НЕТ')
