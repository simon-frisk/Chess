import sys
import math
import pygame
import board
import game
import colors
from agents.user import User
from agents.stupid_bot import StupidBot
from agents.smart_bot import SmartBot
from pieces.piece import PieceColor

pygame.init()

BOX_WIDTH = 70
FPS = 40
font = pygame.font.SysFont(None, 90)

screen_width = BOX_WIDTH * 8
screen_icon = pygame.image.load('pieces/images/W_KING.png')
display_surface = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Chess')
pygame.display.set_icon(screen_icon)

clock = pygame.time.Clock()

player1 = User(PieceColor.WHITE)
player2 = SmartBot(PieceColor.BLACK)
game = game.Game([player1, player2], board.init_pieces(BOX_WIDTH), BOX_WIDTH)

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
    game.render(display_surface, BOX_WIDTH, colors.BLACK, colors.WHITE, font)

    pygame.display.update()

    clock.tick(FPS)
