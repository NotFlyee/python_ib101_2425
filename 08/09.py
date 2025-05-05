text = input()
pos = int(input())
print(text[pos - 1] if pos < len(text) else 'ОШИБКА')
