from particle_cell import ParticleCell

class PoisonCell(ParticleCell):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.increment_amount = 1

    def poison(self):
        return True
