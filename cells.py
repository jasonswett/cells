import pygame, sys, time, random
from pygame.locals import *

def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((1200, 600), 0, 32)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    DEFAULT_CELL_WIDTH = 20

    color_options = [BLUE, YELLOW]

    for yi in range(0, 5):
        y_position = DEFAULT_CELL_WIDTH * yi + 2 * yi

        for xi in range(0, 5):
            color = color_options[random.randint(0, 1)]
            x_position = DEFAULT_CELL_WIDTH * xi + 2 * xi
            pygame.draw.rect(DISPLAY, color, (x_position, y_position, DEFAULT_CELL_WIDTH, DEFAULT_CELL_WIDTH), 0)

    pygame.display.update()
    time.sleep(3)

main()
