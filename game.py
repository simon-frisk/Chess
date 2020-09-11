import pygame
import board
from pieces.piece import PieceColor


class Game:
    def __init__(self, agents, pieces):
        self._agents = agents
        self.pieces = pieces
        self.turn_agent.find_possible_moves(self.pieces)

    @property
    def turn_agent(self):
        return self._agents[0]

    def turn(self, piece, to_box):
        board.move_piece(self.pieces, piece, to_box)
        self._agents.reverse()
        self.turn_agent.find_possible_moves(self.pieces)

    def render(self, surface, box_width, black, white):
        for row in range(0, 8):
            for column in range(0, 8):
                pygame.draw.rect(surface, self.get_box_color(
                    row, column, black, white), (column * box_width, row * box_width, box_width, box_width))

        for piece in self.pieces:
            piece.render(surface)

        turn_line_y = box_width * 8 if self.turn_agent.color == PieceColor.WHITE else 0
        pygame.draw.line(surface, (0, 255, 0), (0, turn_line_y),
                         (8 * box_width, turn_line_y), 5)

        self.turn_agent.render(surface, box_width)

    def get_box_color(self, row, column, black, white):
        if(row % 2):
            if(column % 2):
                return white
            else:
                return black
        else:
            if(column % 2):
                return black
            else:
                return white
