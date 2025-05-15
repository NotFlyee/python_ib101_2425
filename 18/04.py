def continue_fibonacci_sequence(seq, n):
    global sequence
    for i in range(n):
        next_element = seq[-1] + seq[-2]
        seq = seq + [next_element]
    sequence = seq
