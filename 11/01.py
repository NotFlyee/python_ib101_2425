data = []
answer = ''
for i in range(int(input())):
    data.append(int(input()))
n = int(input())
for i in range(len(data)):
    if answer:
        break
    for j in range(i + 1, len(data)):
        if data[i] == data[j]:
            continue
        if data[i] * data[j] == n:
            answer = 'ДА'
            break
print(answer) if answer else print('НЕТ')
