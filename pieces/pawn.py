from pieces.piece import Piece, PieceType, PieceColor


class Pawn(Piece):
    def __init__(self, column, row, color, width):
        super().__init__(column, row, color, PieceType.PAWN, width)

    def possible_moves(self, pieces):
        direction = -1 if self.color == PieceColor.WHITE else 1
        possible_moves = []
        possible_moves += self.step_possible(pieces,
                                             0, 1 * direction, 1, False)
        possible_moves += self.step_possible(pieces,
                                             1, 1 * direction, 1, True, False)
        possible_moves += self.step_possible(pieces, -1,
                                             1 * direction, 1, True, False)
        if direction == 1 and self.row == 1:
            possible_moves += self.step_possible(pieces, 0, 2, 1, False)
        if direction == -1 and self.row == 6:
            possible_moves += self.step_possible(pieces, 0, -2, 1, False)
        return possible_moves
