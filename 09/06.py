m = int(input())
n = int(input())
for i in range(n):
    n = input()
    if len(n) <= m:
        print(n)
    else:
        print(n[:m - 3], '...', sep='')
