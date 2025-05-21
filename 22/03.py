from random import choices
import string

def generate_password(m: int) -> str:
    chars = [char for char in string.ascii_letters + string.digits if char not in ['l', 'I', '1', 'o', 'O', '0']]
    print(chars)
    return ''.join(choices(chars, k=m))

def main(n: int, m: int) -> str:
    return [generate_password(m) for _ in range(n)]
