import pygame, time, random, sys
from pygame.locals import *
from cell_screen import CellScreen
from cell import Cell
from food_cell import FoodCell
from poison_cell import PoisonCell
from organism import Organism
from gene import Gene

def main():
    pygame.init()
    SCREEN_WIDTH = 30
    cell_screen = CellScreen(int(SCREEN_WIDTH * 1.5), SCREEN_WIDTH)

    MAX_ALLOWED_ORGANISMS = 3

    while True:
        organism_width = 6
        organism_height = 6
        organism_x = random.randint(0, cell_screen.width - 1 - organism_width)
        organism_y = random.randint(0, cell_screen.height - 1 - organism_height)
        gene = Gene((organism_width, organism_height))

        organism_candidate = Organism(
                cell_screen,
                (organism_x, organism_y),
                gene
        )

        if not(organism_candidate.conflicts_with_any_of(cell_screen.organisms)):
            print(gene.dna_string)
            cell_screen.organisms.append(organism_candidate)

        if len(cell_screen.organisms) >= MAX_ALLOWED_ORGANISMS:
            break

    cell_screen.draw_organisms()

    world_time = 0

    while True:
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

            world_time += 1
            time.sleep(0.01)

            if world_time % 300 == 0:
                for organism in cell_screen.organisms:
                    organism.age()

            for organism in cell_screen.organisms:
                organism.check_health()

            if len(cell_screen.organisms) == 0:
                sys.exit()

            if touched:
                break

            if cell.off_screen():
                break

main()
