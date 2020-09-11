from pieces.piece import Piece, PieceType


class Rook(Piece):
    def __init__(self, column, row, piece_color):
        super().__init__(column, row, piece_color, PieceType.ROOK)

    def possible_moves(self, pieces):
        possible_move_boxes = []
        possible_move_boxes += self.find_possible_in_direction(pieces, 1, 0)
        possible_move_boxes += self.find_possible_in_direction(pieces, -1, 0)
        possible_move_boxes += self.find_possible_in_direction(pieces, 0, 1)
        possible_move_boxes += self.find_possible_in_direction(pieces, 0, -1)
        return possible_move_boxes
