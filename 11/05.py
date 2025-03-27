soldiers = []
punished = []
n = int(input())
for i in range(n):
    soldiers.append(input())
k = int(input())
m = int(input())
for i in range(k - 1, len(soldiers), k):
    punished.append((soldiers[i]))
for soldier in soldiers:
    if soldier not in punished:
        print(soldier)
