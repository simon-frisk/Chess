import pygame


class Agent:
    def __init__(self, board, color):
        self.board = board
        self.color = color
        self.selected_box = None

    def render(self, surface, BOX_WIDTH):
        if self.selected_box:
            pygame.draw.rect(surface, (0, 255, 0), (self.selected_box['column'] * BOX_WIDTH,
                                                    self.selected_box['row'] * BOX_WIDTH, BOX_WIDTH, BOX_WIDTH), 5)
