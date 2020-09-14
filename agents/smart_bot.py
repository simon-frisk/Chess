from agents.agent import Agent
from pieces.piece import PieceType, PieceColor
import random
import board


class SmartBot(Agent):
    def handle_turn(self, pieces, turn, click, enemy):
        moves = self.possible_moves.copy()
        random.shuffle(moves)

        for possible_move in moves:
            points = 0
            pieces_after_move = board.pieces_after_move(pieces, possible_move)
            enemy_moves = enemy.find_possible_moves(pieces_after_move)
            enemy_color = PieceColor.BLACK if self.color == PieceColor.WHITE else PieceColor.WHITE

            if possible_move['capture']:
                if possible_move['capture'].piece_type == PieceType.QUEEN:
                    points += 4
                if possible_move['capture'].piece_type != PieceType.PAWN:
                    points += 2
            if len(enemy_moves) == 0:
                is_chess = board.is_chess(pieces_after_move, enemy_color)
                if is_chess:
                    points += 10
                else:
                    points -= 10
            for enemy_move in enemy_moves:
                if enemy_move['capture']:
                    if enemy_move['capture'].piece_type == PieceType.QUEEN:
                        points -= 4
                    if enemy_move['capture'].piece_type != PieceType.PAWN:
                        points -= 2
            possible_move['points'] = points

        points = [move['points'] for move in moves]
        max_points = max(points)
        for move in moves:
            if move['points'] == max_points:
                turn(move)
                break
