import random
from agents.agent import Agent


class StupidBot(Agent):
    def handle_turn(self, switch_turn):
        own_pieces = filter(lambda piece: piece.piece_color ==
                            self.color, self.board.pieces)
        possible_moves = [{'piece': piece, 'move': move}
                          for piece in own_pieces for move in piece.calculate_possible_move_boxes()]
        move = random.choice(possible_moves)
        self.board.move_piece(
            move['piece'], move['move']['row'], move['move']['column'])
        switch_turn()
