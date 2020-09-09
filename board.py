import pygame
import math
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.piece import PieceType, PieceColor


class Board:
    BOX_COUNT = 8
    BOX_WIDTH = 70
    BLACK = (80, 40, 20)
    WHITE = (220, 160, 110)

    def __init__(self):
        self.pieces = [
            Rook(self, 0, 0, PieceColor.BLACK),
            Knight(self, 0, 1, PieceColor.BLACK),
            Bishop(self, 0, 2, PieceColor.BLACK),
            Queen(self, 0, 3, PieceColor.BLACK),
            King(self, 0, 4, PieceColor.BLACK),
            Bishop(self, 0, 5, PieceColor.BLACK),
            Knight(self, 0, 6, PieceColor.BLACK),
            Rook(self, 0, 7, PieceColor.BLACK),
            Pawn(self, 1, 0, PieceColor.BLACK),
            Pawn(self, 1, 1, PieceColor.BLACK),
            Pawn(self, 1, 2, PieceColor.BLACK),
            Pawn(self, 1, 3, PieceColor.BLACK),
            Pawn(self, 1, 4, PieceColor.BLACK),
            Pawn(self, 1, 5, PieceColor.BLACK),
            Pawn(self, 1, 6, PieceColor.BLACK),
            Pawn(self, 1, 7, PieceColor.BLACK),
            Pawn(self, 6, 0, PieceColor.WHITE),
            Pawn(self, 6, 1, PieceColor.WHITE),
            Pawn(self, 6, 2, PieceColor.WHITE),
            Pawn(self, 6, 3, PieceColor.WHITE),
            Pawn(self, 6, 4, PieceColor.WHITE),
            Pawn(self, 6, 5, PieceColor.WHITE),
            Pawn(self, 6, 6, PieceColor.WHITE),
            Pawn(self, 6, 7, PieceColor.WHITE),
            Rook(self, 7, 0, PieceColor.WHITE),
            Knight(self, 7, 1, PieceColor.WHITE),
            Bishop(self, 7, 2, PieceColor.WHITE),
            Queen(self, 7, 3, PieceColor.WHITE),
            King(self, 7, 4, PieceColor.WHITE),
            Bishop(self, 7, 5, PieceColor.WHITE),
            Knight(self, 7, 6, PieceColor.WHITE),
            Rook(self, 7, 7, PieceColor.WHITE),
        ]

    def render(self, surface, current_turn_color):
        for row in range(0, self.BOX_COUNT):
            for column in range(0, self.BOX_COUNT):
                pygame.draw.rect(surface, self.get_box_color(
                    row, column), self.get_box_dimensions(row, column))

        for piece in self.pieces:
            piece.render(surface)

        turn_line_y = self.BOX_WIDTH * \
            self.BOX_COUNT if current_turn_color == PieceColor.WHITE else 0
        pygame.draw.line(surface, (0, 255, 0), (0, turn_line_y),
                         (self.BOX_COUNT * self.BOX_WIDTH, turn_line_y), 5)

    def move_piece(self, piece, row, column):
        piece.row = row
        piece.column = column

    def get_piece(self, row, column):
        for piece in self.pieces:
            if(piece.row == row and piece.column == column):
                return piece

    def get_box_color(self, row, column):
        if(row % 2):
            if(column % 2):
                return self.WHITE
            else:
                return self.BLACK
        else:
            if(column % 2):
                return self.BLACK
            else:
                return self.WHITE

    def get_box_dimensions(self, row, column):
        index = row * self.BOX_COUNT + column
        x = index % self.BOX_COUNT * self.BOX_WIDTH
        y = math.floor(index / self.BOX_COUNT) * self.BOX_WIDTH
        return (x, y, self.BOX_WIDTH, self.BOX_WIDTH)
