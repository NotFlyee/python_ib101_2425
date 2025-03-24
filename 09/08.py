n = input()
mx = 0
for p in range(len(n)):
    for q in range(p + 1, len(n) + 1):
        if 'р' not in n[p:q] and len(n[p:q]) > mx:
            mx = len(n[p:q])
print(mx)
