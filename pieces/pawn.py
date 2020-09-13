from pieces.piece import Piece, PieceType, PieceColor
import board


class Pawn(Piece):
    def __init__(self, column, row, color, width):
        super().__init__(column, row, color, PieceType.PAWN, width)
        self.can_be_en_passented = False

    def possible_moves(self, pieces):
        direction = -1 if self.color == PieceColor.WHITE else 1
        steps = 2 if not self.has_moved else 1
        moves = []
        moves += self.step_possible(pieces, 0, direction, steps, False)
        moves += self.step_possible(pieces, 1, direction, 1, True, False)
        moves += self.step_possible(pieces, -1, direction, 1, True, False)

        if self.row == (3 if direction == -1 else 4):
            to_right = board.get_piece(
                pieces, {'row': self.row, 'column': self.column + 1})
            if to_right and to_right.color != self.color and to_right.piece_type == PieceType.PAWN and to_right.can_be_en_passented:
                move = self.step_possible(pieces, 1, direction, 1, False)[0]
                move['capture'] = to_right
                moves.append(move)

            to_left = board.get_piece(
                pieces, {'row': self.row, 'column': self.column - 1})
            if to_left and to_left.color != self.color and to_left.piece_type == PieceType.PAWN and to_left.can_be_en_passented:
                move = self.step_possible(pieces, -1, direction, 1, False)[0]
                move['capture'] = to_left
                moves.append(move)

        return moves
