from random import shuffle
import sys

students = [line.strip() for line in sys.stdin]
temp = students[:]
while not all(map(lambda x: temp.index(x) != students.index(x), students)):
    shuffle(temp)
print(*[f'{students[i]} - {temp[i]}' for i in range(len(students))], sep='\n')
