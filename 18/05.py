def mirror(arr):
    mirrored_part = arr[:]
    mirrored_part.reverse()
    arr += mirrored_part
