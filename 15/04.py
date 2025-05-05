def who_are_you_and_hello():
    name = input()
    while len(name.split()) != 1 or 0 in [1 if 1040 <= ord(char) <= 1103 else 0 for char in name] or name != name.lower().capitalize():
        name = input()
    print(f'Привет, {name}')

