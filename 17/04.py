menu = []
receipt_counter = 1

def add_item(item_name: str, item_cost: int):
    menu.append((item_name, item_cost))

def print_receipt():
    global receipt_counter
    if not menu: return

    print(f'Чек {receipt_counter}. Всего предметов: {len(menu)}')
    for item_name, item_cost in menu:
        print(f'{item_name} - {item_cost}')
    print(f'Итого: {sum([cost for _, cost in menu])}')
    print('-----')

    receipt_counter += 1
    menu.clear()
