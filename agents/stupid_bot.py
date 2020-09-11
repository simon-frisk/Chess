import random
from agents.agent import Agent


class StupidBot(Agent):
    def handle_turn(self, pieces, turn, click):
        own_pieces = filter(lambda piece: piece.color ==
                            self.color, pieces)
        possible_moves = [{'piece': piece, 'move': move}
                          for piece in own_pieces for move in piece.possible_moves(pieces)]
        move = random.choice(possible_moves)
        turn(move['piece'], move['move'])
