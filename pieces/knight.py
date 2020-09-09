from pieces.piece import Piece, PieceType, PieceColor


class Knight(Piece):
    def __init__(self, board, column, row, piece_color):
        super().__init__(board, column, row, piece_color, PieceType.KNIGHT)

    def calculate_possible_move_boxes(self):
        return []
