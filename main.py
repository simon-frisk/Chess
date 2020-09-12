import sys
import math
import pygame
import board
import game
from agents.user import User
from agents.stupid_bot import StupidBot
from pieces.piece import PieceColor

pygame.init()

BOX_WIDTH = 70
BLACK = (80, 40, 20)
WHITE = (220, 160, 110)
font = pygame.font.SysFont(None, 70)


screen_width = BOX_WIDTH * 8
display_surface = pygame.display.set_mode(
    (BOX_WIDTH * 8, BOX_WIDTH * 8))
pygame.display.set_caption('Chess')

clock = pygame.time.Clock()

game = game.Game([User(PieceColor.WHITE),
                  StupidBot(PieceColor.BLACK)], board.init_pieces(BOX_WIDTH), BOX_WIDTH)

while True:
    click = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if type(game.turn_agent) == User:
                row = math.floor(event.pos[1] / BOX_WIDTH)
                column = math.floor(event.pos[0] / BOX_WIDTH)
                click = {'row': row, 'column': column}

    game.handle_turn(game.pieces, click)
    game.render(display_surface, BOX_WIDTH, BLACK, WHITE, font)

    pygame.display.update()

    clock.tick(30)
