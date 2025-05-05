n = int(input())
while n <= 10**9 and str(n)[0] != '1':
    n *= int(str(n)[0])
print(n)
