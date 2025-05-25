from PIL import Image, ImageDraw

def gradient(color: str):
    shade = [0, 0, 0]
    image = Image.new('RGB', (512, 200))
    height = image.size[1]
    draw = ImageDraw.Draw(image)
    for line in range(0, 512, 2):
        shade['rgb'.index(color.lower())] = line // 2
        draw.rectangle((line, 0, line + 2, height), tuple(shade))
    image.save('res.png')

gradient('r')
