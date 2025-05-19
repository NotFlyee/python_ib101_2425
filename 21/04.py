import sys

print(sum(map(lambda x: x.lstrip().startswith('#'), sys.stdin)))
