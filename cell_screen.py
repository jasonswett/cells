import pygame

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

    def fits(self, organism_candidate):
        return True
