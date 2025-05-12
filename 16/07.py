def find_mountain(heights_map: list[list[int]]):
    mx = (0, [])
    for row in heights_map:
        if max(row) > mx[0]:
            mx = (max(row), row)
    return heights_map.index(mx[1]), mx[1].index(max(mx[1]))
