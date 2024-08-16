import numpy as np
import pygame
from pixel import Pixel

GRID_SIZE = 28
width, height = [GRID_SIZE * Pixel.PIXEL_SIZE,] * 2

pixels = list()

for y_cord in range(0, height, Pixel.PIXEL_SIZE):
    for x_cord in range(0, width, Pixel.PIXEL_SIZE):
        pixels.append(Pixel(x_cord, y_cord))

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        for pixel in pixels:
            pixel.update_color(*pygame.mouse.get_pos())

    if pygame.key.get_pressed()[pygame.K_TAB]:
        for pixel in pixels:
            pixel.erase()

    screen.fill((0, 0, 0))
    for pixel in pixels:
        pixel.draw(screen)
    pygame.display.flip()

feature_vector = np.array([pixel.get_value() for pixel in pixels])
print(feature_vector)

pygame.quit()
