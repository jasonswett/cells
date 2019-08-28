import random
from cell import Cell
from hard_cell import HardCell
from soft_cell import SoftCell

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
                if random.randint(0, 1) == 0:
                    self.cells.append(HardCell(x + self.x, y + self.y))
                else:
                    self.cells.append(SoftCell(x + self.x, y + self.y))

    def conflicts_with_any_of(self, organisms):
        for organism in organisms:
            if organism.conflicts_with(self):
                return True
        return False

    def conflicts_with(self, organism):
        for self_cell in self.cells:
            for other_cell in organism.cells:
                if self_cell.occupies_same_space_as(other_cell):
                    return True
        return False

    def is_touched_by(self, other_cell):
        for self_cell in self.cells:
            if self_cell.occupies_same_space_as(other_cell):
                return True
        return False

    def react_to(self, poison_cell):
        for i, cell in enumerate(self.cells):
            if cell.x == poison_cell.x and cell.y == poison_cell.y and cell.hurt_by_poison():
                del self.cells[i]
