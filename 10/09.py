n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
p = int(input())
q = int(input())
_sum = 0
for i in data[p - 1:q]:
    _sum += i
print(_sum)
