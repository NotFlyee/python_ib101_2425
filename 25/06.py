import pymorphy3, sys

parse = pymorphy3.MorphAnalyzer().parse

words = sys.stdin.read().split()
mapped_words = list(map(lambda word: parse(word)[0].tag.animacy, words))

def agree(word1, word2):
    tags = parse(word2)[0].tag
    gender = tags.gender
    number = tags.number
    grammemes = {number, 'nomn'} if number == 'plur' else {gender, 'nomn'}
    return parse(word1)[0].inflect(grammemes).word

for i in range(len(words)):
    word = words[i]
    mapped_word = mapped_words[i]
    if mapped_word == 'anim':
        print(agree('живой', word).capitalize())
    elif mapped_word == 'inan':
        print(f'Не {agree("живой", word)}')
    else:
        print('Не существительное')
