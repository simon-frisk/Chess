from pieces.piece import Piece, PieceType


class Queen(Piece):
    def __init__(self, board, column, row, piece_color):
        super().__init__(board, column, row, piece_color, PieceType.QUEEN)

    def possible_moves(self):
        possible_move_boxes = []
        possible_move_boxes += self.find_possible_in_direction(1, 0)
        possible_move_boxes += self.find_possible_in_direction(-1, 0)
        possible_move_boxes += self.find_possible_in_direction(0, 1)
        possible_move_boxes += self.find_possible_in_direction(0, -1)
        possible_move_boxes += self.find_possible_in_direction(1, 1)
        possible_move_boxes += self.find_possible_in_direction(1, -1)
        possible_move_boxes += self.find_possible_in_direction(-1, 1)
        possible_move_boxes += self.find_possible_in_direction(-1, -1)
        return possible_move_boxes
