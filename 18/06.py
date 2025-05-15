def from_string_to_list(string: str, container: list):
    container += [int(i) for i in string.split()]
