from pieces.piece import Piece, PieceType, PieceColor


class King(Piece):
    def __init__(self, board, column, row, piece_color):
        super().__init__(board, column, row, piece_color, PieceType.KING)

    def possible_moves(self):
        return []
