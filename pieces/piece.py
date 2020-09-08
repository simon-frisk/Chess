import pygame
import enum

pygame.font.init()
FONT = pygame.font.SysFont(None, 40)


class PieceType(enum.Enum):
    PAWN = 'P'
    KING = 'K'
    QUEEN = 'Q'


class PieceColor(enum.Enum):
    WHITE = 'W'
    BLACK = 'B'


class Piece:
    def __init__(self, row, column, piece_color, piece_type):
        self.column = column
        self.row = row
        self.piece_color = piece_color
        self.piece_type = piece_type

    def render(self, surface, get_box_dimensions):
        img = FONT.render(self.piece_color.value +
                          self.piece_type.value, True, (255, 0, 0))
        surface.blit(img, get_box_dimensions(self.row, self.column))
