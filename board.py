import pygame
import math


class Board:

    def __init__(self):
        self.FONT = pygame.font.SysFont(None, 40)
        self.BOX_COUNT = 8
        self.BOX_WIDTH = 70
        self.BLACK = (30, 30, 30)
        self.WHITE = (240, 240, 240)
        self.state = [
            ['BR', 'BK', '', '', '', '', '', 'BR'],
            ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
            ['WR', 'WK', 'WB', '', '', '', '', ''],
        ]

    def render(self, surface):
        for row_index, row_value in enumerate(self.state):
            for col_index, box_value in enumerate(row_value):
                pygame.draw.rect(surface, self.get_box_color(
                    row_index, col_index), self.get_box_dimensions(row_index, col_index))
                img = self.FONT.render(box_value, True, (255, 0, 0))
                surface.blit(img, self.get_box_dimensions(
                    row_index, col_index))

    def get_box_color(self, row_index, col_index):
        if(row_index % 2):
            if(col_index % 2):
                return self.WHITE
            else:
                return self.BLACK
        else:
            if(col_index % 2):
                return self.BLACK
            else:
                return self.WHITE

    def get_box_dimensions(self, row_index, col_index):
        index = row_index * self.BOX_COUNT + col_index
        x = index % self.BOX_COUNT * self.BOX_WIDTH
        y = math.floor(index / self.BOX_COUNT) * self.BOX_WIDTH
        return (x, y, self.BOX_WIDTH, self.BOX_WIDTH)
