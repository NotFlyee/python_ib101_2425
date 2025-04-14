data = []
for i in range(int(input())):
    word = input()
    if 'кот' in word:
        data.append((i + 1, word.index('кот') + 1))
for i in data:
    print(*i)
