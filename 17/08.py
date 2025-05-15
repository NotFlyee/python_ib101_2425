messages = []

def print_only_new(message: str):
    if message in messages:
        return
    print(message)
    messages.append(message)
