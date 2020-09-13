from agents.agent import Agent
import random


class SmartBot(Agent):
    def handle_turn(self, pieces, turn, click):
        move = None
        for possible_move in self.possible_moves:
            if possible_move['capture']:
                move = possible_move
                break

        if not move:
            move = random.choice(self.possible_moves)

        turn(move)
