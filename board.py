import pygame
import math
import copy
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


def move_piece(pieces, move):
    if move['capture']:
        pieces.remove(move['capture'])
    if move['extra']:
        move_piece(pieces, move['extra'])
    move['piece'].row = move['box']['row']
    move['piece'].column = move['box']['column']
    move['piece'].has_moved = True

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
        return move['capture'] == king

    is_chess = any([threatens_king(move) for move in enemy_moves])
    return is_chess


def pieces_after_move(pieces, move):
    ''' Calculates how the pieces would be if a given move was conducted'''
    pieces_copy = [copy.deepcopy(piece) for piece in pieces]
    move_piece = board.get_piece(pieces_copy, {
        'row': move['piece'].row,
        'column': move['piece'].column
    })
    capture_piece = board.get_piece(pieces_copy, {
        'row': move['capture'].row,
        'column': move['capture'].column
    }) if move['capture'] else None
    extra_piece = board.get_piece(pieces_copy, {
        'row': move['extra']['piece'].row,
        'column': move['extra']['piece'].column
    }) if move['extra'] else None
    move_piece(pieces_copy, {
        'piece': move_piece, 'box': move['box'], 'capture': capture_piece, 'extra': {'piece': extra_piece, 'capture': None, 'extra': None, 'box': move['extra']['box']} if move['extra'] else None})
