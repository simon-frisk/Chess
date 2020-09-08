from pieces.piece import Piece, PieceType, PieceColor


class Pawn(Piece):
    def __init__(self, board, column, row, piece_color):
        super().__init__(board, column, row, piece_color, PieceType.PAWN)

    def calculate_possible_move_boxes(self):
        possible_moves = []
        direction = -1 if self.piece_color == PieceColor.WHITE else 1
        if(self.piece_color == PieceColor.WHITE and self.row == self.board.BOX_COUNT - 2 or self.piece_color == PieceColor.BLACK and self.row == 1):
            possible_moves += [{'row': self.row +
                                2 * direction, 'column': self.column}]
        possible_moves += [{'row': self.row +
                            1 * direction, 'column': self.column}]
        return possible_moves
