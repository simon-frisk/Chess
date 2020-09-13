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
                piece = board.get_piece(pieces, board.get_box(row, column))
                if piece:
                    possible = False
                    break
                if board.is_chess(board.pieces_after_move(pieces, board.get_move(self, board.get_box(row, column), None, None)), self.color):
                    possible = False
                    break

            if possible:
                direction = 1 if self.column < rook.column else -1
                extra_move = board.get_move(rook, board.get_box(
                    row, self.column + direction * 2 + direction * -1), None, None)
                move = board.get_move(self, board.get_box(
                    row, self.column + direction * 2), None, extra_move)
                possible_moves.append(move)

        return possible_moves
