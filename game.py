import pygame
import board
import copy
from pieces.piece import PieceColor, PieceType


class Game:
    def __init__(self, agents, pieces, box_width):
        self._agents = agents
        self.pieces = pieces
        self.turn_agent.find_possible_moves(self.pieces)
        pieces = copy.copy(pieces)
        self.load_images(box_width)
        self.chess_mate = False
        self.chess = False

    @property
    def turn_agent(self):
        return self._agents[0]

    def handle_turn(self, pieces, click):
        if not self.chess_mate:
            self.turn_agent.handle_turn(pieces, self.turn, click)

    def turn(self, piece, to_box):
        board.move_piece(self.pieces, piece, to_box)
        self._agents.reverse()
        possible_moves = self.turn_agent.find_possible_moves(self.pieces)
        if len(possible_moves) == 0:
            self.chess_mate = True
        if board.is_chess(self.pieces, self.turn_agent.color):
            self.chess = True
        else:
            self.chess = False

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
        pygame.draw.line(surface, (0, 255, 0), (0, turn_line_y),
                         (8 * box_width, turn_line_y), 5)

        self.turn_agent.render(surface, box_width)

        if self.chess_mate:
            text = font.render('Chessmate', False, (170, 170, 170))
            x = box_width * 4 - text.get_rect().width / 2
            y = box_width * 4 - text.get_rect().height / 2
            surface.blit(text, (x, y))
        elif self.chess:
            text = font.render('Chess', False, (170, 170, 170))
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
