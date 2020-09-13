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
    def __init__(self, row, column, color, piece_type, width):
        self.column = column
        self.row = row
        self.color = color
        self.piece_type = piece_type
        self.width = width
        self.has_moved = False

    def step_possible(self, pieces, column_step_multiplier, row_step_multiplier, step_limit=None, allow_capture=True, allow_non_capture=True):
        moves = []
        while True:
            try_steps = len(moves) + 1
            column = self.column + try_steps * column_step_multiplier
            row = self.row + try_steps * row_step_multiplier
            box = {'row': row, 'column': column}
            piece_there = board.get_piece(pieces, box)
            move = {'piece': self, 'box': box,
                    'capture': piece_there, 'extra': None}

            if not (0 <= row <= 7) or not (0 <= column <= 7):
                break

            piece = board.get_piece(pieces, box)
            if piece and piece.color != self.color and allow_capture:
                moves.append(move)
                break
            if not piece and allow_non_capture:
                moves.append(move)
                if step_limit and len(moves) >= step_limit:
                    break
            else:
                break

        return moves
