import pygame, time, random
from cell_screen import CellScreen
from cell import Cell
from organism import Organism
from pygame.locals import *

def main():
    pygame.init()
    SCREEN_WIDTH = 30
    cell_screen = CellScreen(int(SCREEN_WIDTH * 1.5), SCREEN_WIDTH)

    MAX_ALLOWED_ORGANISMS = 6
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
        pygame.display.update()

    poison_count = 150

    for i in range(0, poison_count):
        poison_cell = Cell(0, cell_screen.random_y(), (255, 0, 0))

        while True:
            touched_by_poison = False
            for organism in organisms:
                if organism.is_touched_by(poison_cell):
                    organism.react_to(poison_cell)
                    cell_screen.draw_organism(organism)
                    touched_by_poison = True

            if not(touched_by_poison):
                cell_screen.draw_cell(poison_cell)

            shadow_cell = Cell(poison_cell.x - 1, poison_cell.y, (0, 0, 0))
            cell_screen.draw_cell(shadow_cell)

            poison_cell.x += 1
            pygame.display.update()

            time.sleep(0.01)

            if touched_by_poison:
                break

            if poison_cell.x >= cell_screen.width + 1:
                break

main()
