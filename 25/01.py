import pymorphy3, sys, string

morph = pymorphy3.MorphAnalyzer()

text = sys.stdin.read().translate(str.maketrans('', '', string.punctuation)).split()
print(sum(map(lambda word: morph.parse(word)[0].normal_form in ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть'], text)))
