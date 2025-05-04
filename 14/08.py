dict = {}
for _ in range(int(input())):
    note = input()
    dict[note[:note.index(' ')]] = note[note.index(' ') + 1:]
for _ in range(int(input())):
    word = input()
    print(dict[word] if word in dict else 'Нет в словаре')
