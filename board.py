import pygame
import math
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.piece import PieceType, PieceColor


def init_pieces():
    return [
        Rook(0, 0, PieceColor.BLACK),
        Knight(0, 1, PieceColor.BLACK),
        Bishop(0, 2, PieceColor.BLACK),
        Queen(0, 3, PieceColor.BLACK),
        King(0, 4, PieceColor.BLACK),
        Bishop(0, 5, PieceColor.BLACK),
        Knight(0, 6, PieceColor.BLACK),
        Rook(0, 7, PieceColor.BLACK),
        Pawn(1, 0, PieceColor.BLACK),
        Pawn(1, 1, PieceColor.BLACK),
        Pawn(1, 2, PieceColor.BLACK),
        Pawn(1, 3, PieceColor.BLACK),
        Pawn(1, 4, PieceColor.BLACK),
        Pawn(1, 5, PieceColor.BLACK),
        Pawn(1, 6, PieceColor.BLACK),
        Pawn(1, 7, PieceColor.BLACK),
        Pawn(6, 0, PieceColor.WHITE),
        Pawn(6, 1, PieceColor.WHITE),
        Pawn(6, 2, PieceColor.WHITE),
        Pawn(6, 3, PieceColor.WHITE),
        Pawn(6, 4, PieceColor.WHITE),
        Pawn(6, 5, PieceColor.WHITE),
        Pawn(6, 6, PieceColor.WHITE),
        Pawn(6, 7, PieceColor.WHITE),
        Rook(7, 0, PieceColor.WHITE),
        Knight(7, 1, PieceColor.WHITE),
        Bishop(7, 2, PieceColor.WHITE),
        Queen(7, 3, PieceColor.WHITE),
        King(7, 4, PieceColor.WHITE),
        Bishop(7, 5, PieceColor.WHITE),
        Knight(7, 6, PieceColor.WHITE),
        Rook(7, 7, PieceColor.WHITE),
    ]


def move_piece(pieces, piece, row, column):
    old_piece = get_piece(pieces, row, column)
    if old_piece:
        pieces.remove(old_piece)

    piece.row = row
    piece.column = column

    return pieces


def get_piece(pieces, row, column):
    for piece in pieces:
        if(piece.row == row and piece.column == column):
            return piece
