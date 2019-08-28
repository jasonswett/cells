import pygame, time, random
from cell_screen import CellScreen
from cell import Cell
from food_cell import FoodCell
from poison_cell import PoisonCell
from organism import Organism
from pygame.locals import *

def main():
    pygame.init()
    SCREEN_WIDTH = 30
    cell_screen = CellScreen(int(SCREEN_WIDTH * 1.5), SCREEN_WIDTH)

    MAX_ALLOWED_ORGANISMS = 10

    while True:
        organism_width = 4
        organism_height = 4
        organism_x = random.randint(0, cell_screen.width - 1 - organism_width)
        organism_y = random.randint(0, cell_screen.height - 1 - organism_height)

        organism_candidate = Organism(
                cell_screen,
                (organism_x, organism_y),
                (organism_width, organism_height)
        )

        if not(organism_candidate.conflicts_with_any_of(cell_screen.organisms)):
            cell_screen.organisms.append(organism_candidate)

        if len(cell_screen.organisms) >= MAX_ALLOWED_ORGANISMS:
            break

    cell_screen.draw_organisms()

    cell_count = 150

    for i in range(0, cell_count):
        if random.randint(0, 1) == 0:
            cell = PoisonCell(cell_screen)
        else:
            cell = FoodCell(cell_screen)

        while True:
            touched = False
            for organism in cell_screen.organisms:
                if organism.is_touched_by(cell):
                    organism.react_to(cell)
                    cell_screen.draw_organism(organism)
                    touched = True

            if not(touched):
                cell_screen.draw_cell(cell)

            cell_screen.draw_cell(Cell(cell.previous_x(), cell.y, (0, 0, 0)))

            cell.advance()
            pygame.display.update()

            time.sleep(0.01)

            if touched:
                break

            if cell.off_screen():
                break

main()
