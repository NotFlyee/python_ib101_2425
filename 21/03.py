import sys

data = [int(i) for i in sys.stdin if i != '\n']
print(sum(data) / len(data) if data else -1)
