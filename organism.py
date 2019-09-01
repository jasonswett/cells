import random
from cell import Cell
from hard_cell import HardCell
from soft_cell import SoftCell
from blank_cell import BlankCell
from gene import Gene

class Organism:
    def __init__(self, cell_screen, position, gene):
        self.cell_screen = cell_screen
        self.x = position[0]
        self.y = position[1]
        self.width = gene.width
        self.height = gene.height

        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        color_options = [BLUE, YELLOW]

        self.cells = []

        for y in range(0, self.height):
            for x in range(0, self.width):
                if gene.at(x, y) == '00':
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

    def react_to(self, foreign_cell):
        for i, self_cell in enumerate(self.cells):
            if self_cell.x == foreign_cell.x and self_cell.y == foreign_cell.y:
                if foreign_cell.poison() and self_cell.hurt_by_poison():
                    self.cells[i] = BlankCell(foreign_cell.x, foreign_cell.y)
                    return
                if foreign_cell.food() and self_cell.helped_by_food():
                    self.grow()
                    return

    def grow(self):
        for i, cell in enumerate(self.cells):
            if cell.blank():
                self.cells[i] = SoftCell(cell.x, cell.y)
                self.cell_screen.draw_organisms()
                return

    def age(self):
        for i, cell in enumerate(self.cells):
            if cell.soft():
                self.cells[i] = BlankCell(cell.x, cell.y)
                self.cell_screen.draw_organisms()
                return

    def check_health(self):
        if self.mortally_ill():
            self.die()

    def mortally_ill(self):
        soft_cell_count = 0
        for cell in self.cells:
            if cell.soft():
                soft_cell_count += 1
        return soft_cell_count < int(len(self.cells) / 4)

    def die(self):
        for i, cell in enumerate(self.cells):
            self.cells[i] = BlankCell(cell.x, cell.y)
        self.cell_screen.draw_organisms()
        self.cell_screen.remove_organism(self)
