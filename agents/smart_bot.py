from agents.agent import Agent
from pieces.piece import PieceType
import random
import board


class SmartBot(Agent):
    def handle_turn(self, pieces, turn, click, enemy):
        moves = self.possible_moves.copy()
        random.shuffle(moves)

        move = None
        for possible_move in moves:
            pieces_after_move = board.pieces_after_move(pieces, possible_move)
            enemy_moves = enemy.find_possible_moves(pieces_after_move)

            is_bad = False
            for enemy_move in enemy_moves:
                if enemy_move['capture']:
                    if enemy_move['capture'].piece_type != PieceType.PAWN:
                        is_bad = True
            if not is_bad:
                move = possible_move
                break

        if not move:
            move = random.choice(self.possible_moves)

        turn(move)
