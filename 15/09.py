def ask_password():
    password = 'password'
    atts = 3
    while atts:
        if input() == password:
            break
        atts -= 1
    print('Пароль принят' if atts else 'В доступе отказано')

