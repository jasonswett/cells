import pygame, time, random, sys
from pygame.locals import *
from cell_screen import CellScreen
from cell import Cell
from food_cell import FoodCell
from poison_cell import PoisonCell
from organism import Organism
from chromosome import Chromosome

def main():
    pygame.init()
    SCREEN_WIDTH = 40
    cell_screen = CellScreen(int(SCREEN_WIDTH * 1.5), SCREEN_WIDTH)

    MAX_ALLOWED_ORGANISMS = 6
    ORGANISM_WIDTH = 8
    ORGANISM_HEIGHT = 8

    for i in range(0, MAX_ALLOWED_ORGANISMS):
        add_organism(cell_screen, Chromosome((ORGANISM_WIDTH, ORGANISM_HEIGHT), ''))

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
            time.sleep(0.001)

            if world_time % 200 == 0:
                for organism in cell_screen.organisms:
                    organism.age()

            for organism in cell_screen.organisms:
                organism.check_health()

            if len(cell_screen.organisms) <= 2:
                parents = []

                for i in range(0, 2):
                    for organism in cell_screen.organisms:
                        parents.append(organism)

                for i in range(0, MAX_ALLOWED_ORGANISMS):
                    add_organism(cell_screen, parents[0].chromosome.offspring_with(parents[1].chromosome))

            if touched:
                break

            if cell.off_screen():
                break

def add_organism(cell_screen, chromosome):
    while True:
        organism_x = random.randint(0, cell_screen.width - 1 - chromosome.width)
        organism_y = random.randint(0, cell_screen.height - 1 - chromosome.height)

        organism_candidate = Organism(
            cell_screen,
            (organism_x, organism_y),
            chromosome
        )

        if not(organism_candidate.conflicts_with_any_of(cell_screen.organisms)):
            print(chromosome.dna_string)
            cell_screen.organisms.append(organism_candidate)
            return

main()
