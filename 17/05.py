data = {}

def add_friends(name_of_person: str, list_of_friends: list[str]):
    data[name_of_person] = list_of_friends

def are_friends(name_of_person1: str, name_of_person2: str):
    return name_of_person2 in data[name_of_person1]

def print_friends(name_of_person: str):
    print(*sorted([name for name in data[name_of_person]]))
