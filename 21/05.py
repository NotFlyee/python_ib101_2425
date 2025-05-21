import sys

print(not all([all(map(int, i.split())) for i in sys.stdin]))
