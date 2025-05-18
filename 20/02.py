def simple_map(transformation, values):
    temp = []
    for el in values:
        temp.append(transformation(el))
    return temp
