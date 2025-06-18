import pymorphy3


def agree_word(number):
    morph = pymorphy3.MorphAnalyzer()
    parse = morph.parse
    return parse('бутылка')[0].make_agree_with_number(number).word


def f(number):
    if number == 0: return
    print(
f'''В холодильнике {number} {agree_word(number)} кваса.
Возьмём одну и выпьем.
Осталось {number - 1} {agree_word(number - 1)} кваса.''')
    f(number - 1)


f(99)
