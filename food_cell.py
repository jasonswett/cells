from particle_cell import ParticleCell

class FoodCell(ParticleCell):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 255, 0)
        self.increment_amount = 1

    def food(self):
        return True
