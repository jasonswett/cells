import random

class Chromosome:
    def __init__(self, size, dna_string):
        self.GENE_LENGTH = 2
        self.width = size[0]
        self.height = size[1]

        self.dna_string = dna_string

        if self.dna_string == '':
            for i in range(0, self.width * self.height):
                self.dna_string += '0' + str(random.randint(0, 1))

    def at(self, x, y):
        position_for_cell = (x * self.width + y) * self.GENE_LENGTH
        return self.dna_string[position_for_cell:position_for_cell + self.GENE_LENGTH]

    def offspring_with(self, other_chromosome):
        midway_point = random.randint(0, len(self.dna_string))
        left = self.dna_string[0:midway_point]
        right = other_chromosome.dna_string[midway_point:len(other_chromosome.dna_string)]
        return Chromosome((self.width, self.height), left + right)
