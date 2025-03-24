str1 = input()
str2 = input()
cows, bulls = 0, 0
for i in range(len(str1)):
    if str1[i] == str2[i]:
        bulls += 1
    elif str1[i] in str2:
        cows += 1
print(bulls, cows)
