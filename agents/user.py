import pygame
import board
from agents.agent import Agent


class User(Agent):

    def handle_turn(self, pieces, turn, click):
        if not click:
            return

        is_possible_box = None
        for box in self.possible_from_selected:
            if box == click:
                is_possible_box = True
                break

        if is_possible_box:
            piece = board.get_piece(pieces, self.selected)
            self.selected = None
            self.possible_from_selected = []
            turn(piece, click)

        else:
            piece = board.get_piece(pieces, click)
            if piece and piece.color == self.color:
                self.selected = click
                self.possible_from_selected = piece.possible_moves(pieces)
            else:
                self.selected = None
                self.possible_from_selected = []
