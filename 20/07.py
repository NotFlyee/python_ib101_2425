def same_by(characteristic, objects: list[int]):
    if not objects:
        return True
    return not (len(set(map(characteristic, objects))) - 1)
