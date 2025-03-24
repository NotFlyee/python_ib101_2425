n = input()
for c in n:
    if not (97 <= ord(c) <= 122 or 48 <= ord(c) <= 57 or ord(c) == 95):
        print('Неверный символ:', c)
        break
