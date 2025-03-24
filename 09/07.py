n = int(input())
counter = 1
for i in range(n):
    n = input()
    if 'кот' in n:
        for j in range(len(n)):
            if n[j:j+3] == 'кот':
                print(counter, j + 1)
    counter += 1
