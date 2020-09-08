import pygame
from agents.agent import Agent
from pieces.piece import PieceColor


class User(Agent):

    def handle_box_click(self, row, column):
        piece = self.board.get_piece(row, column)
        print(piece)
        if piece and piece.piece_color == PieceColor.WHITE:
            self.selected_box = {'row': row, 'column': column}
