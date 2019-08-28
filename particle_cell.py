from cell import Cell

class ParticleCell(Cell):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def advance(self):
        self.x += self.increment_amount

    def previous_x(self):
        return self.x - self.increment_amount
