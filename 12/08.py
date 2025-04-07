url = input()
key = input()
get_reqs = url.split('?')[1].split('&')
keys = [tuple(req.split('=')) for req in get_reqs]
print(''.join([value[1] for value in keys if value[0] == key]))
