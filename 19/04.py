def partial_sums(*args):
    temp = []
    for i in range(0, len(args) + 1):
        temp.append(sum(args[0:i]))
    return temp
