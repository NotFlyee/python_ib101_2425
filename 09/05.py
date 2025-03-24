n = int(input())
for i in range(n):
    n = input()
    if n[:2] == 'не' or n[:2] == 'Не':
        print(n[3:])
    else:
        print(n)
