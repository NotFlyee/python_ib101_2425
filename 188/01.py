phrases = []

def parrot(phrase: str):
    if phrase in phrases:
        print(phrase)
    phrases.append(phrase)
