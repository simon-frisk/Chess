from pieces.piece import Piece, PieceType, PieceColor


class Pawn(Piece):
    def __init__(self, board, column, row, piece_color):
        super().__init__(board, column, row, piece_color, PieceType.PAWN)

    def possible_moves(self):
        direction = -1 if self.piece_color == PieceColor.WHITE else 1
        possible_move_boxes = []
        possible_move_boxes += self.find_possible_in_direction(
            0, 1 * direction, 1, False)
        possible_move_boxes += self.find_possible_in_direction(
            1, 1 * direction, 1, True, False)
        possible_move_boxes += self.find_possible_in_direction(
            -1, 1 * direction, 1, True, False)
        if direction == 1 and self.row == 1:
            possible_move_boxes += self.find_possible_in_direction(
                0, 2, 1, False)
        if direction == -1 and self.row == self.board.BOX_COUNT - 2:
            possible_move_boxes += self.find_possible_in_direction(
                0, -2, 1, False)
        return possible_move_boxes
