costs = []
numbers = []
pos_costs = []
mistakes = []
n = input()
amount = int(n[:4])
total_sum = int(n[4:])
for i in range(amount):
    n = input()
    costs.append(int(n[:7]))
    numbers.append(int(n[8:11]))
    pos_costs.append(int(n[13:]))
_sum = 0
for i in range(amount):
    _sum += costs[i] * numbers[i]
print(total_sum - _sum)
for i in range(amount):
    if costs[i] * numbers[i] != pos_costs[i]:
        print(i + 1, end=' ')
