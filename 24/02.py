from PIL import Image, ImageDraw

def get_equally_resized_images(image1, image2):
    max_size = max(image1.size, image2.size)
    return image1.resize(max_size), image2.resize(max_size)

def transparency(ﬁlename1: str, ﬁlename2: str):
    image1, image2 = get_equally_resized_images(Image.open(filename1), Image.open(filename2))
    pixels1, pixels2 = image1.load(), image2.load()
    width, height = image1.size
    new_image = Image.new('RGB', (width, height))
    pixels3 = new_image.load()
    for x in range(width):
        for y in range(height):
            r1, g1, b1 = pixels1[x, y]
            r2, g2, b2 = pixels2[x, y]
            r, g, b = int(r1 * 0.5 + r2 * 0.5), int(g1 * 0.5 + g2 * 0.5), int(b1 * 0.5 + b2 * 0.5)
            pixels3[x, y] = r, g, b

    new_image.save('res.jpg')
