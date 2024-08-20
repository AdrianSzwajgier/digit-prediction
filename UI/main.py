import pygame

from UI.display import Display
from services.process_data import get_data, read_labels_file


class UI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Display.width, Display.height))
        self.display = Display()
        pygame.display.set_caption("Simple Pygame Window")
        self.images = get_data("train-images.idx3-ubyte")
        self.labels = read_labels_file("train-labels.idx1-ubyte")
        self.image_id = -1

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.image_id += 1
                        self.display.display_image(self.images[self.image_id])

            if pygame.mouse.get_pressed()[0]:
                self.display.mouse_draw(pygame.mouse.get_pos())

            if pygame.key.get_pressed()[pygame.K_TAB]:
                self.display.erase()

            self.screen.fill((0, 0, 0))
            self.display.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

    def get_feature_vector(self):
        return self.display.get_feature_vector()


if __name__ == "__main__":
    ui = UI()
    ui.main()
