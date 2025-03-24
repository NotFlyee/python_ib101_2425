n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
for i in range(len(data) - 1):
    print(data[i] + data[i + 1])
