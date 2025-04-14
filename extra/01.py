text = input()

br = '({[)}]'
temp = []
an = 'YES'

for i in text:
    pos = br.index(i)
    if pos <= 2: 
        temp.append(i)
    elif len(temp) == 0 or br[pos - 3] != temp.pop():
        an = 'NO'
print(an)
