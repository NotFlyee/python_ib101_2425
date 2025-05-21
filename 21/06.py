import sys
data = [i for i in sys.stdin]
for i in range(len(data)):
    line = data[i].strip()
    if line.lstrip().startswith('#'):
        print(f'Line {i + 1}: {line[2:]}')
