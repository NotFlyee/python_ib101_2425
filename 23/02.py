from PIL import Image

image = Image.open('p_23_01.jpg')
pixels = image.load()
x, y = image.size

r, g, b = 0, 0, 0

for i in range(x):
    for j in range(y):
        _r, _g, _b = pixels[i, j]
        r += _r
        g += _g
        b += _b

print(r // (x*y), g // (x*y), b // (x*y))
