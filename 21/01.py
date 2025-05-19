string = input().split()
print(*sorted(string, key=lambda x: x.lower()))
