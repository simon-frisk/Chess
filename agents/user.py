import pygame
from agents.agent import Agent


class User(Agent):

    def handle_box_click(self, row, column):
        clicked_possible_move_box = None
        for possible_move_box in self.possible_move_boxes:
            if(possible_move_box['row'] == row and possible_move_box['column'] == column):
                clicked_possible_move_box = possible_move_box
                break

        if clicked_possible_move_box:
            piece = self.board.get_piece(
                self.selected_box['row'], self.selected_box['column'])
            self.board.move_piece(piece, row, column)
            self.selected_box = None
            self.possible_move_boxes = []

        else:
            piece = self.board.get_piece(row, column)
            if piece and piece.piece_color == self.color:
                self.selected_box = {'row': row, 'column': column}
                self.possible_move_boxes = piece.calculate_possible_move_boxes()
            else:
                self.selected_box = None
                self.possible_move_boxes = []
