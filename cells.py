import pygame, sys, time, random
from pygame.locals import *

DEFAULT_CELL_WIDTH = 20
TOTAL_CELL_WIDTH = DEFAULT_CELL_WIDTH + 2

class CellScreen:
    def __init__(self, width, height):
        self.DEFAULT_CELL_WIDTH = 20
        self.width = width
        self.height = height
        width_in_pixels = TOTAL_CELL_WIDTH * width
        height_in_pixels = TOTAL_CELL_WIDTH * height
        self.display = pygame.display.set_mode((width_in_pixels, height_in_pixels), 0, 32)

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

        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        color_options = [BLUE, YELLOW]

        self.cell_colors = []
        for i in range(0, self.width * self.height):
            color = color_options[random.randint(0, 1)]
            self.cell_colors.append(color)

    def show(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.cell_screen.draw_cell(self.x + x, self.y + y, self.cell_colors[y + (x * y)])

def main():
    pygame.init()
    cell_screen = CellScreen(30, 30)

    organism_count = 4
    organisms = []

    for i in range(0, organism_count):
        organism_width = 6
        organism_height = 6
        organism_x = random.randint(0, cell_screen.width - 1 - organism_width)
        organism_y = random.randint(0, cell_screen.height - 1 - organism_height)
        organisms.append(Organism(cell_screen, (organism_x, organism_y), (organism_width, organism_height)))

    for organism in organisms:
        organism.show()

    poison_count = 5

    for i in range(0, poison_count):
        poison_x = 0
        poison_y = random.randint(0, cell_screen.height - 1)
        RED = (255, 0, 0)

        while True:
            cell_screen.draw_cell(poison_x, poison_y, RED)
            cell_screen.draw_cell(poison_x - 1, poison_y, (0, 0, 0))
            poison_x += 1
            time.sleep(0.02)

            pygame.display.update()

            if poison_x >= cell_screen.width + 1:
                break

main()
