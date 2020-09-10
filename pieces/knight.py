from pieces.piece import Piece, PieceType, PieceColor


class Knight(Piece):
    def __init__(self, board, column, row, piece_color):
        super().__init__(board, column, row, piece_color, PieceType.KNIGHT)

    def possible_moves(self):
        possible_move_boxes = []
        possible_move_boxes += self.find_possible_in_direction(1, 2, 1)
        possible_move_boxes += self.find_possible_in_direction(-1, 2, 1)
        possible_move_boxes += self.find_possible_in_direction(1, -2, 1)
        possible_move_boxes += self.find_possible_in_direction(-1, -2, 1)
        possible_move_boxes += self.find_possible_in_direction(2, 1, 1)
        possible_move_boxes += self.find_possible_in_direction(2, -1, 1)
        possible_move_boxes += self.find_possible_in_direction(-2, 1, 1)
        possible_move_boxes += self.find_possible_in_direction(-2, -1, 1)
        return possible_move_boxes
