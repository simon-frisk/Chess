import random
from agents.agent import Agent


class StupidBot(Agent):
    def handle_turn(self, pieces, turn, click, enemy):
        move = random.choice(self.possible_moves)
        turn(move)
