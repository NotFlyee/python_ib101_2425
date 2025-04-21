numbers = {}
for _ in range(int(input())):
    number, name = input().split()
    numbers[number] = name
for _ in range(int(input())):
    name = input()
    temp = []
    if name not in numbers.values():
        print('Нет в телефонной книге')
        continue
    for number, _name in numbers.items():
        if _name == name:
            temp.append(number)
    print(*temp, sep=' ')
