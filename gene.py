import random

class Gene:
    def __init__(self, size):
        self.CHROMOSOME_LENGTH = 2
        self.width = size[0]
        self.height = size[1]
        self.dna_string = ''

        for i in range(0, self.width * self.height):
            self.dna_string += '0' + str(random.randint(0, 1))

    def at(self, x, y):
        position_for_cell = (x * self.width + y) * self.CHROMOSOME_LENGTH
        return self.dna_string[position_for_cell:position_for_cell + self.CHROMOSOME_LENGTH]
