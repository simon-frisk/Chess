from pieces.piece import Piece, PieceType


class Queen(Piece):
    def __init__(self, board, column, row, piece_color):
        super().__init__(board, column, row, piece_color, PieceType.QUEEN)

    def calculate_possible_move_boxes(self):
        possible_move_boxes = []
        possible_move_boxes += self.find_possible_moves_in_direction({'row': self.row - 1, 'column': self.column}, lambda coordinate: {
            'row': coordinate['row'] - 1, 'column': coordinate['column']})
        possible_move_boxes += self.find_possible_moves_in_direction({'row': self.row + 1, 'column': self.column}, lambda coordinate: {
            'row': coordinate['row'] + 1, 'column': coordinate['column']})
        possible_move_boxes += self.find_possible_moves_in_direction({'row': self.row + 1, 'column': self.column + 1}, lambda coordinate: {
            'row': coordinate['row'] + 1, 'column': coordinate['column'] + 1})

        return possible_move_boxes

    def find_possible_moves_in_direction(self, coordinate, move_function):
        piece_on_current_box = self.board.get_piece(
            coordinate['row'], coordinate['column'])
        is_box_valid = 0 <= coordinate['row'] <= self.board.BOX_COUNT and 0 <= coordinate[
            'column'] <= self.board.BOX_COUNT
        if piece_on_current_box or not is_box_valid:
            return []
        else:
            next_box_coordinate = move_function(coordinate)
            next_boxes = self.find_possible_moves_in_direction(
                next_box_coordinate, move_function)
            return next_boxes + [coordinate]
