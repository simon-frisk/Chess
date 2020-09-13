import pygame
import board
import copy
import colors
from pieces.piece import PieceType

SELECTED_OUTLINE_WIDTH = 5


class Agent:
    def __init__(self, color):
        self.color = color
        self.selected = None
        self.possible_from_selected = []
        self.possible_moves = []

    def render(self, surface, BOX_WIDTH):
        for possible_move in self.possible_from_selected:
            pygame.draw.rect(surface, colors.LIGHT_GREEN, (possible_move['box']['column'] * BOX_WIDTH,
                                                           possible_move['box']['row'] * BOX_WIDTH, BOX_WIDTH, BOX_WIDTH), SELECTED_OUTLINE_WIDTH)
        if self.selected:
            pygame.draw.rect(surface, colors.DARK_GREEN, (self.selected['column'] * BOX_WIDTH,
                                                          self.selected['row'] * BOX_WIDTH, BOX_WIDTH, BOX_WIDTH), SELECTED_OUTLINE_WIDTH)

    def find_possible_moves(self, pieces):
        own_pieces = [piece for piece in pieces if piece.color == self.color]
        possible_moves = [
            move for piece in own_pieces for move in piece.possible_moves(pieces)]

        legal_moves = []
        for move in possible_moves:
            after_move = board.pieces_after_move(pieces, move)
            if not board.is_chess(after_move, self.color):
                legal_moves.append(move)

        self.possible_moves = legal_moves
        return self.possible_moves
