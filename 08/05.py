prev = input()
while True:
    new = input()
    if new[0] != prev[-1]:
        break
    prev = new
print(new)
