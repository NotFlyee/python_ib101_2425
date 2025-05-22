phrases = set()

def parrot(phrase: str) -> str:
    global phrases
    if phrase in phrases:
        print(phrase)
    phrases.add(phrase)
