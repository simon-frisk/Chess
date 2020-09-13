import pygame
import board
from agents.agent import Agent


class User(Agent):
    def handle_turn(self, pieces, turn, click, enemy):
        if not click:
            return

        selected_move = None
        for move in self.possible_from_selected:
            if move['box'] == click:
                selected_move = move
                break

        if selected_move:
            self.selected = None
            self.possible_from_selected = []
            turn(selected_move)

        else:
            piece = board.get_piece(pieces, click)
            if piece and piece.color == self.color:
                self.selected = click
                self.possible_from_selected = [move for move in filter(
                    lambda move: move['piece'] == piece, self.possible_moves)]
            else:
                self.selected = None
                self.possible_from_selected = []
