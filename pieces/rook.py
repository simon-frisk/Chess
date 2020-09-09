from pieces.piece import Piece, PieceType


class Rook(Piece):
    def __init__(self, board, column, row, piece_color):
        super().__init__(board, column, row, piece_color, PieceType.ROOK)

    def calculate_possible_move_boxes(self):
        return [{'row': self.row, 'column': self.column + 1}]
