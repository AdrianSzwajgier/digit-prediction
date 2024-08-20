from math import sqrt, pow

import pygame


def distance_to_float(distance, threshold1=14, threshold2=30):
    if distance < threshold1:
        return 1.0
    elif distance < threshold2:
        return 1.0 - (distance - threshold1) / (threshold2 - threshold1)
    else:
        return 0.0


class Pixel:
    PIXEL_SIZE = 20
    BLACK = (0, 0, 0)
    GRAY = (64, 64, 64)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.border_rect = pygame.Rect(x, y, self.PIXEL_SIZE, self.PIXEL_SIZE)
        self.inner_rect = pygame.Rect(x+1, y+1, self.PIXEL_SIZE-2, self.PIXEL_SIZE-2)
        self.color = self.BLACK
        self.value = 0

    def cursor_distance(self, mouse_x, mouse_y):
        return sqrt(pow(self.x - mouse_x, 2) + pow(self.y - mouse_y, 2))

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        self.color = (value * 255, ) * 3

    def get_color(self):
        return self.color[0]

    def set_color(self, shade):
        self.value = shade / 255
        self.color = (shade, ) * 3

    def update_color(self, mouse_x, mouse_y):
        distance = self.cursor_distance(mouse_x, mouse_y)
        value = distance_to_float(distance)
        gray_scale = value * 255
        if gray_scale > self.color[0]:
            self.value = value
            self.color = (gray_scale,) * 3

    def erase(self):
        self.color = self.BLACK
        self.value = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.GRAY, self.border_rect)
        pygame.draw.rect(surface, self.color, self.inner_rect)
