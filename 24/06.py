from PIL import Image

def make_preview(size: tuple[int], n_colors: int):
    image = Image.open('p_24_17.jpg')
    width, height = image.size
    new_image = image.resize(size).quantize(n_colors)

    new_image.save('res.bmp')
