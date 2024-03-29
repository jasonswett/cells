import pygame, random

INNER_CELL_WIDTH = 8
CELL_WIDTH = INNER_CELL_WIDTH + 2

class CellScreen:
    def __init__(self, width, height):
        self.organisms = []
        self.width = width
        self.height = height
        width_in_pixels = CELL_WIDTH * width
        height_in_pixels = CELL_WIDTH * height
        self.display = pygame.display.set_mode((width_in_pixels, height_in_pixels), 0, 32)

    def draw_cell(self, cell):
        x_position = cell.x * CELL_WIDTH
        y_position = cell.y * CELL_WIDTH
        pygame.draw.rect(self.display, cell.color, (x_position, y_position, INNER_CELL_WIDTH, INNER_CELL_WIDTH), 0)

    def draw_organism(self, organism):
        for cell in organism.cells:
            self.draw_cell(cell)

    def random_y(self):
        return random.randint(0, self.height - 1)

    def draw_organisms(self):
        for organism in self.organisms:
            self.draw_organism(organism)
        pygame.display.update()

    def remove_organism(self, organism):
        for i, self_organism in enumerate(self.organisms):
            if self_organism == organism:
                del self.organisms[i]
