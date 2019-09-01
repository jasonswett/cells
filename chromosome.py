import random

class Chromosome:
    def __init__(self, size):
        self.GENE_LENGTH = 2
        self.width = size[0]
        self.height = size[1]
        self.dna_string = ''

        for i in range(0, self.width * self.height):
            self.dna_string += '0' + str(random.randint(0, 1))

    def at(self, x, y):
        position_for_cell = (x * self.width + y) * self.GENE_LENGTH
        return self.dna_string[position_for_cell:position_for_cell + self.GENE_LENGTH]
