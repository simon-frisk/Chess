from pieces.piece import Piece, PieceType


class Pawn(Piece):
    def __init__(self, column, row, piece_color):
        super().__init__(column, row, piece_color, PieceType.PAWN)
