import sys
data = [i.strip() for i in sys.stdin]
sums = [sum(map(lambda x: ord(x) - ord('A') + 1, i.upper())) for i in data]
print(*sorted(data, key=lambda x: [sums[data.index(x)], x]), sep='\n')
