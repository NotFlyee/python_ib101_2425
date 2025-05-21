friends = dict()

def add_friend(name_of_person: str, name_of_friend: str):
    global friends
    current_friends = friends.get(name_of_person, set())
    current_friends.add(name_of_friend)
    friends[name_of_person] = current_friends


def add_friends(name_of_person: str, list_of_friends: list[str]):
    global friends
    for friend in list_of_friends:
        add_friend(name_of_person, friend)
        add_friend(friend, name_of_person)


def are_friends(name_of_person1: str, name_of_person2: str):
    return name_of_person2 in friends.get(name_of_person1, set())


def print_friends(name_of_person: str):
    print(*sorted([name for name in friends.get(name_of_person, set())]))
