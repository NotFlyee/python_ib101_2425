base = ["Иван", "Юлия Иванкова"]

def hello(name: str):
    print(f'Здравствуйте, {name}! Вашу карту ищут...')

def search_card(name: str):
    print(f'Ваша карта с номером {base.index(name) + 1} найдена' if name in base else 'Ваша карта не найдена')
