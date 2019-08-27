import pygame, time, random
from cell_screen import CellScreen
from organism import Organism
from pygame.locals import *

def main():
    pygame.init()
    cell_screen = CellScreen(30, 30)

    MAX_ALLOWED_ORGANISMS = 4
    organisms = []

    while True:
        organism_width = 6
        organism_height = 6
        organism_x = random.randint(0, cell_screen.width - 1 - organism_width)
        organism_y = random.randint(0, cell_screen.height - 1 - organism_height)

        organism_candidate = Organism(
                cell_screen,
                (organism_x, organism_y),
                (organism_width, organism_height)
        )

        if cell_screen.fits(organism_candidate):
            organisms.append(organism_candidate)

        if len(organisms) >= MAX_ALLOWED_ORGANISMS:
            break

    for organism in organisms:
        organism.show()

    poison_count = 5

    for i in range(0, poison_count):
        poison_x = 0
        poison_y = random.randint(0, cell_screen.height - 1)
        RED = (255, 0, 0)

        while True:
            cell_screen.draw_cell(poison_x, poison_y, RED)
            cell_screen.draw_cell(poison_x - 1, poison_y, (0, 0, 0))
            poison_x += 1
            time.sleep(0.02)

            pygame.display.update()

            if poison_x >= cell_screen.width + 1:
                break

main()
