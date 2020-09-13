from pieces.piece import Piece, PieceType, PieceColor
import board


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

        castle_rooks = []
        row = 0 if self.color == PieceColor.BLACK else 7
        for piece in pieces:
            if piece.color == self.color and piece.piece_type == PieceType.ROOK and not piece.has_moved:
                castle_rooks.append(piece)

        for rook in castle_rooks:
            lowest_column = min(rook.column + 1, self.column + 1)
            highest_column = max(rook.column, self.column)
            possible = True
            for column in range(lowest_column, highest_column):
                # TODO: King cannot be checked and cannot castle through attacked box. Rook can though
                piece = board.get_piece(pieces, {'row': row, 'column': column})
                if piece:
                    possible = False
            if possible:
                direction = 1 if self.column < rook.column else -1
                move = {'piece': self, 'box': {'row': row, 'column': self.column + direction * 2}, 'capture': None, 'extra': {
                    'piece': rook, 'box': {'row': row, 'column': self.column + direction * 2 + direction * -1}, 'capture': None, 'extra': None}}
                possible_moves.append(move)

        return possible_moves
