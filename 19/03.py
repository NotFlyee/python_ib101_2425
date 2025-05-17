def encrypt_caesar(msg: str, shift: int):
    temp = ''
    for char in msg:
        if not 'А' <= char <= 'я':
            temp += char
        elif char <= 'Я':
            temp += chr(ord('А') + (ord(char) + shift - ord('А')) % 32)
        else:
            temp += chr(ord('а') + (ord(char) + shift - ord('а')) % 32)
    return temp

def decrypt_caesar(msg: str, shift: int):
    temp = ''
    for char in msg:
        if not 'А' <= char <= 'я':
            temp += char
        elif char <= 'Я':
            temp += chr(ord('А') + (ord(char) - shift - ord('А')) % 32)
        else:
            temp += chr(ord('а') + (ord(char) - shift - ord('а')) % 32)
    return temp 
