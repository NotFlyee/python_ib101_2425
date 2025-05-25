from PIL import Image, ImageDraw

def board(num: int, size: int):
    image = Image.new('RGB', (num * size, num * size), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for y in range(0, num * size, size * 2):
        for x in range(0, num * size, size * 2):
            draw.rectangle((x, y, x + size, y + size), 'black')
        for x in range(size, (num + 1) * size, size * 2):
            draw.rectangle((x, y + size, x + size, y + size * 2), 'black')

    image.save('res.png')
