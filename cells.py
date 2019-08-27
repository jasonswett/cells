import pygame, sys, time, random
from pygame.locals import *

DEFAULT_CELL_WIDTH = 20
TOTAL_CELL_WIDTH = DEFAULT_CELL_WIDTH + 2

class CellScreen:
    def __init__(self, width, height):
        self.DEFAULT_CELL_WIDTH = 20
        screen_width = TOTAL_CELL_WIDTH * width
        screen_height = TOTAL_CELL_WIDTH * height
        self.display = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    def draw_cell(self, x, y, color):
        x_position = x * TOTAL_CELL_WIDTH
        y_position = y * TOTAL_CELL_WIDTH
        pygame.draw.rect(self.display, color, (x_position, y_position, self.DEFAULT_CELL_WIDTH, self.DEFAULT_CELL_WIDTH), 0)

class Organism:
    def __init__(self, cell_screen, position, size):
        self.cell_screen = cell_screen
        self.x = position[0]
        self.y = position[1]
        self.width = size[0]
        self.height = size[1]

    def show(self):
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        color_options = [BLUE, YELLOW]

        for yi in range(0, self.height):
            for xi in range(0, self.width):
                color = color_options[random.randint(0, 1)]
                self.cell_screen.draw_cell(self.x + xi, self.y + yi, color)

def main():
    pygame.init()
    screen_width = 40
    screen_height = 20
    cell_screen = CellScreen(screen_width, screen_height)

    organism_size = 6
    organism_x = random.randint(0, screen_width - organism_size)
    organism_y = random.randint(0, screen_height - organism_size)
    organism = Organism(cell_screen, (organism_x, organism_y), (organism_size, organism_size))
    organism.show()
    pygame.display.update()
    time.sleep(2)

main()
