data = []
for i in range(int(input())):
    n = input()
    data.append((n[:-2], int(n[-1])))
for kid in data:
    last_name, grade = kid
    print(last_name, grade)
print('')
for kid in data:
    last_name, grade = kid
    if grade >= 4:
        print(last_name, grade)
