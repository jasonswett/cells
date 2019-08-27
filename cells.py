import pygame, sys, time, random
from pygame.locals import *

class CellScreen:
    def __init__(self, width, height):
        self.DEFAULT_CELL_WIDTH = 20
        self.display = pygame.display.set_mode((self.DEFAULT_CELL_WIDTH * width, self.DEFAULT_CELL_WIDTH * height), 0, 32)

    def draw_cell(self, x, y, color):
        x_position = x * self.DEFAULT_CELL_WIDTH + 2 * x
        y_position = y * self.DEFAULT_CELL_WIDTH + 2 * y
        pygame.draw.rect(self.display, color, (x_position, y_position, self.DEFAULT_CELL_WIDTH, self.DEFAULT_CELL_WIDTH), 0)

class Organism:
    def __init__(self, cell_screen, width, height):
        self.cell_screen = cell_screen
        self.width = width
        self.height = height

    def show(self):
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        color_options = [BLUE, YELLOW]

        for yi in range(0, self.height):
            for xi in range(0, self.width):
                color = color_options[random.randint(0, 1)]
                self.cell_screen.draw_cell(xi, yi, color)

def main():
    pygame.init()
    cell_screen = CellScreen(40, 20)

    organism = Organism(cell_screen, 6, 6)
    organism.show()
    pygame.display.update()
    time.sleep(2)

main()
