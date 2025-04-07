words = input().split()
print(' '.join([words[i] for i in [i for i in range(2, len(words), 3)]]))
