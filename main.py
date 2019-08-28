import pygame, time, random
from cell_screen import CellScreen
from cell import Cell
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

        if not(organism_candidate.conflicts_with_any_of(organisms)):
            organisms.append(organism_candidate)

        if len(organisms) >= MAX_ALLOWED_ORGANISMS:
            break

    for organism in organisms:
        cell_screen.draw_organism(organism)

    poison_count = 3

    for i in range(0, poison_count):
        poison_cell = Cell(0, cell_screen.random_y(), (255, 0, 0))

        while True:
            cell_screen.draw_cell(poison_cell)

            shadow_cell = Cell(poison_cell.x - 1, poison_cell.y, (0, 0, 0))
            cell_screen.draw_cell(shadow_cell)

            poison_cell.x += 1
            pygame.display.update()

            time.sleep(0.08)

            if poison_cell.x >= cell_screen.width + 1:
                break

main()
