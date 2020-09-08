import pygame
import math
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.piece import PieceType, PieceColor


class Board:
    BOX_COUNT = 8
    BOX_WIDTH = 70
    BLACK = (30, 30, 30)
    WHITE = (240, 240, 240)

    def __init__(self):
        self.pieces = [
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
            Queen(self, 5, 4, PieceColor.WHITE),
        ]

    def render(self, surface):
        for row in range(0, self.BOX_COUNT):
            for column in range(0, self.BOX_COUNT):
                pygame.draw.rect(surface, self.get_box_color(
                    row, column), self.get_box_dimensions(row, column))

        for piece in self.pieces:
            piece.render(surface)

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
