def main(login: str, password: str):
    ask_password(login, password, lambda login: print(f'Привет, {login}!'), lambda login, err: print(f'Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {err.upper()}.'))

def ask_password(login: str, password: str, success, failure):
    transform = lambda x, y: list(filter(lambda char: char in x, y))
    number_of_vowels = len(transform('aeiouy', list(password)))
    consonants_in_password = transform('qwrtpsdfghjklzxcvbnm', list(password)) 
    constants_in_login = transform('qwrtpsdfghjklzxcvbnm', list(login))
    if number_of_vowels != 3 and consonants_in_password != constants_in_login:
        return failure(login, 'Everything is wrong')
    if number_of_vowels != 3:
        return failure(login, 'Wrong number of vowels')
    if consonants_in_password != constants_in_login:
        return failure(login, 'Wrong consonants')
    return success(login)
