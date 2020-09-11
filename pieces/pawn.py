from pieces.piece import Piece, PieceType, PieceColor


class Pawn(Piece):
    def __init__(self, column, row, piece_color):
        super().__init__(column, row, piece_color, PieceType.PAWN)

    def possible_moves(self, pieces):
        direction = -1 if self.piece_color == PieceColor.WHITE else 1
        possible_move_boxes = []
        possible_move_boxes += self.find_possible_in_direction(pieces,
                                                               0, 1 * direction, 1, False)
        possible_move_boxes += self.find_possible_in_direction(pieces,
                                                               1, 1 * direction, 1, True, False)
        possible_move_boxes += self.find_possible_in_direction(pieces,
                                                               -1, 1 * direction, 1, True, False)
        if direction == 1 and self.row == 1:
            possible_move_boxes += self.find_possible_in_direction(pieces,
                                                                   0, 2, 1, False)
        if direction == -1 and self.row == 6:
            possible_move_boxes += self.find_possible_in_direction(pieces,
                                                                   0, -2, 1, False)
        return possible_move_boxes
