coords = []
max_points = 1
for _ in range(int(input())):
    x, y = input().split()
    coords.append((int(x), int(y)))
for i in coords:
    counter = 1
    for j in coords:
        xi, yi = i
        xj, yj = j
        if i == j or xi // 10 != xj // 10 or yi // 10 != yj // 10:
            continue
        counter += 1
    max_points = max(max_points, counter)
print(max_points)
