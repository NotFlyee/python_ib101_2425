import pymorphy3, sys, string

data = dict()

morph = pymorphy3.MorphAnalyzer()
text = sys.stdin.read().translate(str.maketrans('', '', string.punctuation)).split()
parse = morph.parse

for word in map(lambda word: parse(word)[0].normal_form, filter(lambda word: parse(word)[0].score > 0.5 and 'NOUN' in parse(word)[0].tag, text)):
    if word in data:
        data[word] += 1
    else:
        data[word] = 1

print(*sorted(data, key=lambda word: [-data[word], [-ord(i) for i in word]])[:10])
