# мне не понравилось, всё работает через ж, ей богу. Хер разберешься с stack
import numpy as np
from PIL import Image


def bw_convert(file_name: str) -> None:
    img = np.asarray(Image.open(file_name))
    C = np.round(0.2989 * img[:, :, 0] + 0.5870 * img[:, :, 1] + 0.1140 * img[:, :, 2]).astype(np.uint8)
    Image.fromarray(np.stack([C, C, C], axis=2)).save('res.jpg')
