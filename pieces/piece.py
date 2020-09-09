import pygame
import enum

pygame.font.init()
FONT = pygame.font.SysFont(None, 40)


class PieceType(enum.Enum):
    PAWN = 'PAWN'
    ROOK = 'ROOK'
    KNIGHT = 'KNIGHT'
    BISHOP = 'BISHOP'
    KING = 'KING'
    QUEEN = 'QUEEN'


class PieceColor(enum.Enum):
    WHITE = 'W'
    BLACK = 'B'


class Piece:
    def __init__(self, board, row, column, piece_color, piece_type):
        self.column = column
        self.row = row
        self.piece_color = piece_color
        self.piece_type = piece_type
        self.board = board
        image = pygame.image.load(
            f'./pieces/images/{piece_color.value}_{piece_type.value}.png')
        image = pygame.transform.scale(
            image, (board.BOX_WIDTH, board.BOX_WIDTH))
        self.image = image

    def render(self, surface):
        surface.blit(self.image, self.board.get_box_dimensions(
            self.row, self.column))
