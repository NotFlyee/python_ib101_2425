n = int(input())
data = []
search = []
for i in range(n):
    data.append(input())
for i in range(int(input())):
    search.append(input())
for text in data:
    counter = 0
    for el in search:
        if el in text:
            counter += 1
    if counter == len(search):
        print(text)
