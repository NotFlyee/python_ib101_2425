def print_statistics(arr):
    temp = sorted(arr)
    print(len(arr))
    print(sum(arr) / len(arr) if arr else 0)
    print(min(arr) if arr else 0)
    print(max(arr) if arr else 0)
    print(int(temp[len(temp) // 2] if len(temp) % 2 else sum(temp[len(temp) // 2 - 1:len(temp) // 2 + 1]) / 2))


print_statistics([])
print_statistics([22])
