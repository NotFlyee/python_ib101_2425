last_message = ''

def print_without_duplicates(message):
    global last_message
    if last_message != message: 
        print(message)
    last_message = message
