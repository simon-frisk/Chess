import pygame
import board
import copy
from pieces.piece import PieceType

SELECTED_OUTLINE_WIDTH = 5


class Agent:
    def __init__(self, color):
        self.color = color
        self.selected = None
        self.possible_from_selected = []
        self.possible_moves = []

    def render(self, surface, BOX_WIDTH):
        for possible_move_box in self.possible_from_selected:
            pygame.draw.rect(surface, (200, 100, 100), (possible_move_box['column'] * BOX_WIDTH,
                                                        possible_move_box['row'] * BOX_WIDTH, BOX_WIDTH, BOX_WIDTH), SELECTED_OUTLINE_WIDTH)
        if self.selected:
            pygame.draw.rect(surface, (0, 200, 0), (self.selected['column'] * BOX_WIDTH,
                                                    self.selected['row'] * BOX_WIDTH, BOX_WIDTH, BOX_WIDTH), SELECTED_OUTLINE_WIDTH)

    def find_possible_moves(self, pieces):
        own_pieces = [piece for piece in pieces if piece.color == self.color]
        possible_moves = [{'piece': piece, 'move': move}
                          for piece in own_pieces for move in piece.possible_moves(pieces)]

        legal_moves = []
        for move in possible_moves:
            pieces_copy = [copy.deepcopy(piece) for piece in pieces]
            move_piece = board.get_piece(pieces_copy, {
                'row': move['piece'].row,
                'column': move['piece'].column
            })
            board.move_piece(pieces_copy, move_piece, move['move'])
            if not board.is_chess(pieces_copy, self.color):
                legal_moves.append(move)

        self.possible_moves = legal_moves
        return self.possible_moves
