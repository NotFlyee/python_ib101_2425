def same_by(characteristic, objects: list[int]):
    if not objects:
        return True
    return len(set(map(characteristic, objects))) == 1
