from pieces.piece import Piece, PieceType, PieceColor


class Knight(Piece):
    def __init__(self, column, row, piece_color):
        super().__init__(column, row, piece_color, PieceType.KNIGHT)

    def possible_moves(self, pieces):
        possible_move_boxes = []
        possible_move_boxes += self.find_possible_in_direction(pieces, 1, 2, 1)
        possible_move_boxes += self.find_possible_in_direction(
            pieces, -1, 2, 1)
        possible_move_boxes += self.find_possible_in_direction(
            pieces, 1, -2, 1)
        possible_move_boxes += self.find_possible_in_direction(
            pieces, -1, -2, 1)
        possible_move_boxes += self.find_possible_in_direction(pieces, 2, 1, 1)
        possible_move_boxes += self.find_possible_in_direction(
            pieces, 2, -1, 1)
        possible_move_boxes += self.find_possible_in_direction(
            pieces, -2, 1, 1)
        possible_move_boxes += self.find_possible_in_direction(
            pieces, -2, -1, 1)
        return possible_move_boxes
