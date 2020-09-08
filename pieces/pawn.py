from pieces.piece import Piece, PieceType, PieceColor


class Pawn(Piece):
    def __init__(self, board, column, row, piece_color):
        super().__init__(board, column, row, piece_color, PieceType.PAWN)

    def calculate_possible_move_boxes(self):
        direction = -1 if self.piece_color == PieceColor.WHITE else 1
        return [{'row': self.row + 1 * direction, 'column': self.column}]
