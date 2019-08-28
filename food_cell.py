from cell import Cell

class FoodCell(Cell):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 255, 0)

    def food(self):
        return True
