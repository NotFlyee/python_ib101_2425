def find_farthest_orbit(list_of_orbits: list[int | float]):
    S = [a * b if a != b else 0 for a, b in list_of_orbits] # PI можно не учитывать, т.к. это константа
    return list_of_orbits[S.index(max(S))]
