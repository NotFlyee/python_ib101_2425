def main(login: str, password: str):
    ask_password(login, password, lambda login: print(f'Привет, {login}!'), lambda login, err: print(f'Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {err.upper()}.'))

def ask_password(login: str, password: str, success, failure):
    to_vowels = lambda x, y: list(filter(lambda char: char in x, y))
    to_consonants = lambda x, y: list(filter(lambda char: char not in x, y))
    number_of_vowels = len(to_vowels('aeiouy', list(password.lower())))
    consonants_in_password = to_consonants('aeiouy', list(password.lower())) 
    consonants_in_login = to_consonants('aeiouy', list(login.lower()))
    if number_of_vowels != 3 and consonants_in_password != consonants_in_login:
        return failure(login, 'Everything is wrong')
    if number_of_vowels != 3:
        return failure(login, 'Wrong number of vowels')
    if consonants_in_password != consonants_in_login:
        return failure(login, 'Wrong consonants')
    return success(login)
