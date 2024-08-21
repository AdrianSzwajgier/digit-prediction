import numpy as np

from UI.pixel import Pixel


class Display:
    grid_size = 28
    width, height = (grid_size * Pixel.PIXEL_SIZE, ) * 2

    def __init__(self):
        self.pixels = [
            Pixel(x_cord, y_cord)
            for y_cord in range(0, self.height, Pixel.PIXEL_SIZE)
            for x_cord in range(0, self.width, Pixel.PIXEL_SIZE)
        ]

    def display_image(self, image_data):
        for pixel, value in zip(self.pixels, image_data):
            pixel.set_color(value * 255)

    def mouse_draw(self, mouse_pos):
        for pixel in self.pixels:
            pixel.update_color(*mouse_pos)

    def erase(self):
        for pixel in self.pixels:
            pixel.erase()

    def draw(self, surface):
        for pixel in self.pixels:
            pixel.draw(surface)

    def get_feature_vector(self):
        n = np.array([pixel.get_value() for pixel in self.pixels]).reshape(28, 28, 1)[np.newaxis, ...]
        print(n)
        return n
