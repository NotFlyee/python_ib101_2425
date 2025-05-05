step = int(input())
text = input()
new_text = ''
for char in text:
    new_text += chr(ord(char) + step) if 1040 <= ord(char) <= 1103 else char
print(new_text)
