import random

class Organism:
    def __init__(self, cell_screen, position, size):
        self.cell_screen = cell_screen
        self.x = position[0]
        self.y = position[1]
        self.width = size[0]
        self.height = size[1]

        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        color_options = [BLUE, YELLOW]

        self.cell_colors = []
        for i in range(0, self.width * self.height):
            color = color_options[random.randint(0, 1)]
            self.cell_colors.append(color)

    def show(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.cell_screen.draw_cell(self.x + x, self.y + y, self.cell_colors[y + (x * y)])
