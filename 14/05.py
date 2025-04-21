birthdays = {}
for _ in range(int(input())):
    name, day, month = input().split()
    birthdays[name] = {'day': int(day), 'month': month}
for _ in range(int(input())):
    q = input()
    names = []
    for name in birthdays:
        if birthdays[name]['month'] == q:
            names.append(name)
    print(*sorted(names))
