from pieces.piece import Piece, PieceType, PieceColor


class Pawn(Piece):
    def __init__(self, column, row, color, width):
        super().__init__(column, row, color, PieceType.PAWN, width)

    def possible_moves(self, pieces):
        direction = -1 if self.color == PieceColor.WHITE else 1
        steps = 2 if not self.has_moved else 1
        moves = []
        moves += self.step_possible(pieces, 0, 1 * direction, steps, False)
        moves += self.step_possible(pieces, 1, 1 * direction, 1, True, False)
        moves += self.step_possible(pieces, -1, 1 * direction, 1, True, False)
        return moves
