from PIL import Image, ImageDraw

def twist_image(input_ﬁle_name: str, output_ﬁle_name: str):
    image = Image.open(input_file_name)
    width, height = image.size
    left_side, right_side = image.crop((0, 0, width * 0.5, height)), image.crop((width * 0.5, 0, width, height))
    new_image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(new_image)

    new_image.paste(right_side)
    new_image.paste(left_side, (int(width * 0.5), 0))

    new_image.save(output_file_name)
