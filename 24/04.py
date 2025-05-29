from PIL import Image, ImageFilter

def motion_blur(n: int):
    image = Image.open('p_24_17.jpg')
    new_image = image.transpose(Image.ROTATE_270).filter(ImageFilter.GaussianBlur(n))

    new_image.save('res.jpg')
