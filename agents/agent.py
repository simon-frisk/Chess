import pygame

MARKED_BOX_LINE_WIDTH = 5


class Agent:
    def __init__(self, color):
        self.color = color
        self.selected_box = None
        self.selected_box_moves = []

    def render(self, surface, BOX_WIDTH):
        for possible_move_box in self.selected_box_moves:
            pygame.draw.rect(surface, (200, 100, 100), (possible_move_box['column'] * BOX_WIDTH,
                                                        possible_move_box['row'] * BOX_WIDTH, BOX_WIDTH, BOX_WIDTH), MARKED_BOX_LINE_WIDTH)
        if self.selected_box:
            pygame.draw.rect(surface, (0, 200, 0), (self.selected_box['column'] * BOX_WIDTH,
                                                    self.selected_box['row'] * BOX_WIDTH, BOX_WIDTH, BOX_WIDTH), MARKED_BOX_LINE_WIDTH)
