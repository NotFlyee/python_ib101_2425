text = input()
data = {}
for word in text.split():
    if word not in data:
        data[word] = 0
    data[word] += 1
    print(data[word], end=' ')
