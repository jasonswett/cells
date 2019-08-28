class Cell:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def occupies_same_space_as(self, other_cell):
        return self.x == other_cell.x and self.y == other_cell.y
