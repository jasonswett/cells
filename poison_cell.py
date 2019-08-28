from cell import Cell

class PoisonCell(Cell):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)

    def poison(self):
        return True
