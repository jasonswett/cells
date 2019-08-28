import pygame

INNER_CELL_WIDTH = 20
CELL_WIDTH = INNER_CELL_WIDTH + 2

class CellScreen:
    def __init__(self, width, height):
        self.INNER_CELL_WIDTH = 20
        self.width = width
        self.height = height
        width_in_pixels = CELL_WIDTH * width
        height_in_pixels = CELL_WIDTH * height
        self.display = pygame.display.set_mode((width_in_pixels, height_in_pixels), 0, 32)

    def draw_cell(self, x, y, color):
        x_position = x * CELL_WIDTH
        y_position = y * CELL_WIDTH
        pygame.draw.rect(self.display, color, (x_position, y_position, self.INNER_CELL_WIDTH, self.INNER_CELL_WIDTH), 0)

    def fits(self, organism_candidate):
        return True

    def draw_organism(self, organism):
        for cell in organism.cells:
            self.draw_cell(cell.x, cell.y, cell.color)
