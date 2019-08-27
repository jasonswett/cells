import pygame, sys, time, random
from pygame.locals import *

class CellScreen:
    def __init__(self, width, height):
        DEFAULT_CELL_WIDTH = 20
        self.display = pygame.display.set_mode((DEFAULT_CELL_WIDTH * width, DEFAULT_CELL_WIDTH * height), 0, 32)

class Organism:
    def __init__(self, cell_screen, width, height):
        self.cell_screen = cell_screen
        self.width = width
        self.height = height

    def show(self):
        DEFAULT_CELL_WIDTH = 20

        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        color_options = [BLUE, YELLOW]

        for yi in range(0, self.height):
            y_position = DEFAULT_CELL_WIDTH * yi + 2 * yi

            for xi in range(0, self.width):
                color = color_options[random.randint(0, 1)]
                x_position = DEFAULT_CELL_WIDTH * xi + 2 * xi
                pygame.draw.rect(self.cell_screen.display, color, (x_position, y_position, DEFAULT_CELL_WIDTH, DEFAULT_CELL_WIDTH), 0)

def main():
    pygame.init()
    cell_screen = CellScreen(40, 20)

    organism = Organism(cell_screen, 6, 6)
    organism.show()

    pygame.display.update()
    time.sleep(3)

main()
