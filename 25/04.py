import pymorphy3

morph = pymorphy3.MorphAnalyzer()

word = morph.parse(input())[0]
is_noun = 'NOUN' in word.tag

def agree(word, case, is_plural):
    grammemes = {case, 'plur'} if is_plural else {case}
    return word.inflect(grammemes).word

if is_noun:
    print(
f'''Единственное число:
Именительный падеж: {agree(word, 'nomn', False)}
Родительный падеж: {agree(word, 'gent', False)}
Дательный падеж: {agree(word, 'datv', False)}
Винительный падеж: {agree(word, 'accs', False)}
Творительный падеж: {agree(word, 'ablt', False)}
Предложный падеж: {agree(word, 'loct', False)}
Множественное число:
Именительный падеж: {agree(word, 'nomn', True)}
Родительный падеж: {agree(word, 'gent', True)}
Дательный падеж: {agree(word, 'datv', True)}
Винительный падеж: {agree(word, 'accs', True)}
Творительный падеж: {agree(word, 'ablt', True)}
Предложный падеж: {agree(word, 'loct', True)}''')
else:
    print('Не существительное')
