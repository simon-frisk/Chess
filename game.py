import pygame
import board
import time
import copy
import colors
from pieces.piece import PieceColor, PieceType


class Game:
    def __init__(self, agents, pieces, box_width):
        self._agents = agents
        self.pieces = pieces
        self.turn_agent.find_possible_moves(self.pieces)
        self.load_images(box_width)
        self.game_end = False
        self.event = ''
        self.event_start_time = None
        self.moves_since_capture = 0

    @property
    def turn_agent(self):
        return self._agents[0]

    def handle_turn(self, pieces, click):
        if not self.game_end:
            self.turn_agent.handle_turn(
                pieces, self.turn, click, self._agents[1])

    def turn(self, move):
        self.event = ''
        board.move_piece(self.pieces, move)
        self.moves_since_capture += 1
        if move['capture']:
            self.moves_since_capture = 0
        if self.moves_since_capture >= 50:
            self.event_start_time = time.time()
            self.set_event('Draw')
        self._agents.reverse()
        possible_moves = self.turn_agent.find_possible_moves(self.pieces)
        is_chess = board.is_chess(self.pieces, self.turn_agent.color)
        if is_chess:
            self.set_event('Chess')
        if len(possible_moves) == 0:
            if is_chess:
                self.set_event('Checkmate')
            else:
                self.set_event('Stalemate')

    def set_event(self, event):
        self.event_start_time = time.time()
        self.event = event
        if event == 'Checkmate' or event == 'Stalemate' or event == 'Draw':
            self.game_end = True

    def render(self, surface, box_width, black, white, font):
        for row in range(0, 8):
            for column in range(0, 8):
                pygame.draw.rect(surface, self.get_box_color(
                    row, column, black, white), (column * box_width, row * box_width, box_width, box_width))

        for piece in self.pieces:
            image = self.images[f'{piece.color.value}_{piece.piece_type.value}']
            surface.blit(image, (piece.column * box_width,
                                 piece.row * box_width, box_width, box_width))

        turn_line_y = box_width * 8 if self.turn_agent.color == PieceColor.WHITE else 0
        pygame.draw.line(surface, colors.LIGHT_GREEN, (0, turn_line_y),
                         (8 * box_width, turn_line_y), 12)

        self.turn_agent.render(surface, box_width)

        if self.event and time.time() - self.event_start_time < 10:
            text = font.render(self.event, False, colors.LIGHT_GREEN)
            x = box_width * 4 - text.get_rect().width / 2
            y = box_width * 4 - text.get_rect().height / 2
            surface.blit(text, (x, y))

    def get_box_color(self, row, column, black, white):
        if(row % 2):
            if(column % 2):
                return white
            else:
                return black
        else:
            if(column % 2):
                return black
            else:
                return white

    def load_images(self, width):
        images = {}
        for piece_type in PieceType:
            white = pygame.image.load(
                f'./pieces/images/W_{piece_type.value}.png')
            black = pygame.image.load(
                f'./pieces/images/B_{piece_type.value}.png')
            white = pygame.transform.scale(white, (width, width))
            black = pygame.transform.scale(black, (width, width))
            images.update({f'W_{piece_type.value}': white,
                           f'B_{piece_type.value}': black})
        self.images = images
