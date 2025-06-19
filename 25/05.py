import pymorphy3

morph = pymorphy3.MorphAnalyzer()

word = morph.parse(input())[0]
is_verb = 'INFN' in word.tag or 'VERB' in word.tag

def agree(word, grammemes):
    return word.inflect(grammemes).word

if is_verb:
    print(
f'''Прошедшее время:
{agree(word, {'past', 'masc'})}
{agree(word, {'past', 'femn'})}
{agree(word, {'past', 'neut'})}
{agree(word, {'past', 'plur'})}
Настоящее время:
{agree(word, {'pres', '1per'})}
{agree(word, {'pres', '1per', 'plur'})}
{agree(word, {'pres', '2per'})}
{agree(word, {'pres', '2per', 'plur'})}
{agree(word, {'pres', '3per'})}
{agree(word, {'pres', '3per', 'plur'})}''')
else:
    print('Не глагол')
