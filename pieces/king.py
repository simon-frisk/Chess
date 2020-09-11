from pieces.piece import Piece, PieceType, PieceColor


class King(Piece):
    def __init__(self, column, row, color, width):
        super().__init__(column, row, color, PieceType.KING, width)

    def possible_moves(self, pieces):
        possible_moves = []
        possible_moves += self.step_possible(pieces, 1, 0, 1)
        possible_moves += self.step_possible(pieces, -1, 0, 1)
        possible_moves += self.step_possible(pieces, 0, 1, 1)
        possible_moves += self.step_possible(pieces, 0, -1, 1)
        possible_moves += self.step_possible(pieces, 1, 1, 1)
        possible_moves += self.step_possible(pieces, 1, -1, 1)
        possible_moves += self.step_possible(pieces, -1, 1, 1)
        possible_moves += self.step_possible(pieces, -1, -1, 1)
        return possible_moves
