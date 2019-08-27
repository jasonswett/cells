import random
from cell import Cell

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

        self.cells = []

        for y in range(0, self.height):
            for x in range(0, self.width):
                cell = Cell(x, y, color_options[random.randint(0, 1)])
                self.cells.append(cell)

