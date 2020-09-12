import pygame
import math
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.piece import PieceType, PieceColor


def init_pieces(width):
    return [
        Rook(0, 0, PieceColor.BLACK, width),
        Knight(0, 1, PieceColor.BLACK, width),
        Bishop(0, 2, PieceColor.BLACK, width),
        Queen(0, 3, PieceColor.BLACK, width),
        King(0, 4, PieceColor.BLACK, width),
        Bishop(0, 5, PieceColor.BLACK, width),
        Knight(0, 6, PieceColor.BLACK, width),
        Rook(0, 7, PieceColor.BLACK, width),
        Pawn(1, 0, PieceColor.BLACK, width),
        Pawn(1, 1, PieceColor.BLACK, width),
        Pawn(1, 2, PieceColor.BLACK, width),
        Pawn(1, 3, PieceColor.BLACK, width),
        Pawn(1, 4, PieceColor.BLACK, width),
        Pawn(1, 5, PieceColor.BLACK, width),
        Pawn(1, 6, PieceColor.BLACK, width),
        Pawn(1, 7, PieceColor.BLACK, width),
        Pawn(6, 0, PieceColor.WHITE, width),
        Pawn(6, 1, PieceColor.WHITE, width),
        Pawn(6, 2, PieceColor.WHITE, width),
        Pawn(6, 3, PieceColor.WHITE, width),
        Pawn(6, 4, PieceColor.WHITE, width),
        Pawn(6, 5, PieceColor.WHITE, width),
        Pawn(6, 6, PieceColor.WHITE, width),
        Pawn(6, 7, PieceColor.WHITE, width),
        Rook(7, 0, PieceColor.WHITE, width),
        Knight(7, 1, PieceColor.WHITE, width),
        Bishop(7, 2, PieceColor.WHITE, width),
        Queen(7, 3, PieceColor.WHITE, width),
        King(7, 4, PieceColor.WHITE, width),
        Bishop(7, 5, PieceColor.WHITE, width),
        Knight(7, 6, PieceColor.WHITE, width),
        Rook(7, 7, PieceColor.WHITE, width),
    ]


def move_piece(pieces, piece, box):
    old_piece = get_piece(pieces, box)
    if old_piece:
        pieces.remove(old_piece)

    piece.row = box['row']
    piece.column = box['column']

    return pieces


def get_piece(pieces, box):
    for piece in pieces:
        if(piece.row == box['row'] and piece.column == box['column']):
            return piece


def is_chess(pieces, color):
    for piece in pieces:
        if piece.color == color and piece.piece_type == PieceType.KING:
            king = piece
            break
    enemy_pieces = [piece for piece in pieces if piece.color != color]
    enemy_moves = [
        move for piece in enemy_pieces for move in piece.possible_moves(pieces)]

    def threatens_king(move):
        return move['row'] == king.row and move['column'] == king.column

    is_chess = any([threatens_king(move) for move in enemy_moves])
    return is_chess
