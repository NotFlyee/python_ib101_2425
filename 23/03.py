from PIL import Image, ImageDraw

def picture(file_name: str, width: int, height: int, sky_color: str='#87CEEB', ocean_color: str='#017B92', boat_color: str='#874535', sail_color: str='#FFFFFF', sun_color: str='#FFCF40'):
    image = Image.new('RGB', (width, height), sky_color)
    draw = ImageDraw.Draw(image)
    draw.ellipse((width * 0.8, -(height * 0.2), width * 1.2, height * 0.2), sun_color)
    draw.polygon((width * 0.51, height * 0.3, width * 0.66, height * 0.45, width * 0.51, height * 0.6), sail_color)
    draw.rectangle((0, height * 0.8, width, height), ocean_color)
    draw.rectangle((width * 0.49, height * 0.3, width * 0.51, height * 0.65), boat_color)
    draw.polygon((width * 0.25, height * 0.65, width * 0.75, height * 0.65, width * 0.7, height * 0.85, width * 0.3, height * 0.85), boat_color)

    image.save(file_name)
