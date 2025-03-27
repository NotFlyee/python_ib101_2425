data = []
n = int(input())
for i in range(n):
    data.append(input())
for i in range(n):
    for j in range(i + 1, n):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
for i in data:
    print(i)
