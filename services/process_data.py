import struct
from array import array
import numpy as np


def _read_image_file(filename):
    with open(f"data/{filename}", 'rb') as file:
        magic, size, rows, cols = struct.unpack(">IIII", file.read(16))
        if magic != 2051:
            raise ValueError(
                f"Magic number mismatch, expected 2051, got {magic}"
            )
        image_data = array("B", file.read())
    return image_data, size, rows, cols


def read_labels_file(filename):
    with open(f"data/{filename}", 'rb') as file:
        magic, size = struct.unpack(">II", file.read(8))
        if magic != 2049:
            raise ValueError(
                f"Magic number mismatch, expected 2049, got {magic}"
            )
        return array("B", file.read())


def get_data(filename):
    image_data, size, rows, cols = _read_image_file(filename)
    images = list()
    for i in range(size):
        img = np.array(image_data[i * rows * cols:(i + 1) * rows * cols])
        # img = img.reshape(28, 28)
        images.append(img)
    return images
