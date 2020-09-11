import pygame
import board
from agents.agent import Agent


class User(Agent):

    def handle_turn(self, pieces, turn, click):
        if not click:
            return

        clicked_possible_move_box = None
        for possible_move_box in self.selected_box_moves:
            if(possible_move_box['row'] == click['row'] and possible_move_box['column'] == click['column']):
                clicked_possible_move_box = possible_move_box
                break

        if clicked_possible_move_box:
            piece = board.get_piece(pieces,
                                    self.selected_box['row'], self.selected_box['column'])
            self.selected_box = None
            self.selected_box_moves = []
            turn(piece, click['row'], click['column'])

        else:
            piece = board.get_piece(pieces, click['row'], click['column'])
            if piece and piece.piece_color == self.color:
                self.selected_box = click
                self.selected_box_moves = piece.possible_moves(pieces)
            else:
                self.selected_box = None
                self.selected_box_moves = []
