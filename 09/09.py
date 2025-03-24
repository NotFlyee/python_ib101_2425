n = int(input())
for i in range(n):
    n = input()
    if n[:2] == '%%':
        print(n[2:])
    elif n[:4] == '####':
        continue
    else:
        print(n)
