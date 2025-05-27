def main(login: str, password: str):
    ask_password(login, password, lambda login: print(f'Привет, {login}!'), lambda login, err: print(f'Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {err.upper()}.'))

def ask_password(login: str, password: str, success, failure):
    VOWELS = 'aeiouy'
    to_vowels = lambda x: list(filter(lambda char: char in VOWELS, x))
    to_consonants = lambda x: list(filter(lambda char: char not in VOWELS, x))
    number_of_vowels = len(to_vowels(list(password.lower())))
    consonants_in_password = to_consonants(list(password.lower())) 
    consonants_in_login = to_consonants(list(login.lower()))
    if number_of_vowels != 3 and consonants_in_password != consonants_in_login:
        return failure(login, 'Everything is wrong')
    if number_of_vowels != 3:
        return failure(login, 'Wrong number of vowels')
    if consonants_in_password != consonants_in_login:
        return failure(login, 'Wrong consonants')
    return success(login)
