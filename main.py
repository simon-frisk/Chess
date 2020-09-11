import sys
import math
import pygame
import board
import game
from agents.user import User
from agents.stupid_bot import StupidBot
from pieces.piece import PieceColor

BOX_WIDTH = 70
BLACK = (80, 40, 20)
WHITE = (220, 160, 110)

pygame.init()

screen_width = board.BOX_WIDTH * 8
display_surface = pygame.display.set_mode(
    (board.BOX_WIDTH * 8, board.BOX_WIDTH * 8))
pygame.display.set_caption('Chess')

clock = pygame.time.Clock()

game = game.Game([User(PieceColor.WHITE),
                  StupidBot(PieceColor.BLACK)], board.init_pieces())

while True:
    click = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if type(game.turn_agent) == User:
                row = math.floor(event.pos[1] / board.BOX_WIDTH)
                column = math.floor(event.pos[0] / board.BOX_WIDTH)
                click = {'row': row, 'column': column}

    game.turn_agent.handle_turn(game.pieces, game.turn, click)
    game.render(display_surface, BOX_WIDTH, BLACK, WHITE)

    pygame.display.update()

    clock.tick(30)
