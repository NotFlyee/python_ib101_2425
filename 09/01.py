mn, mx = '', ''
while True:
    n = input()
    if n == 'стоп':
        break
    if not (mx or mn):
        mn, mx = n, n
    if len(n) > len(mx):
        mx = n
    elif len(n) < len(mn):
        mn = n
print(mn, mx)
