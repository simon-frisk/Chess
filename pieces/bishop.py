from pieces.piece import Piece, PieceType, PieceColor


class Bishop(Piece):
    def __init__(self, board, column, row, piece_color):
        super().__init__(board, column, row, piece_color, PieceType.BISHOP)

    def calculate_possible_move_boxes(self):
        return []
