import pygame
import enum
import board

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
    def __init__(self, row, column, piece_color, piece_type):
        self.column = column
        self.row = row
        self.piece_color = piece_color
        self.piece_type = piece_type
        image = pygame.image.load(
            f'./pieces/images/{piece_color.value}_{piece_type.value}.png')
        image = pygame.transform.scale(
            image, (board.BOX_WIDTH, board.BOX_WIDTH))
        self.image = image

    def render(self, surface):
        surface.blit(self.image, (self.column * board.BOX_WIDTH,
                                  self.row * board.BOX_WIDTH, board.BOX_WIDTH, board.BOX_WIDTH))

    def find_possible_in_direction(self, pieces, column_step_multiplier, row_step_multiplier, step_limit=None, allow_capture=True, allow_non_capture=True):
        possible_boxes = []
        while True:
            try_steps = len(possible_boxes) + 1
            column = self.column + try_steps * column_step_multiplier
            row = self.row + try_steps * row_step_multiplier

            if not (0 <= row <= 7) or not (0 <= column <= 7):
                break

            piece = board.get_piece(pieces, row, column)
            if piece and piece.piece_color != self.piece_color and allow_capture:
                possible_boxes.append({'row': row, 'column': column})
                break
            if not piece and allow_non_capture:
                possible_boxes.append({'row': row, 'column': column})
                if step_limit and len(possible_boxes) >= step_limit:
                    break
            else:
                break

        return possible_boxes
