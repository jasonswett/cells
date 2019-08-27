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

        for i in range(0, self.width * self.height):
            cell = Cell(color_options[random.randint(0, 1)])
            self.cells.append(cell)

    def show(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.cell_screen.draw_cell(self.x + x, self.y + y, self.cells[y + (x * y)].color)
