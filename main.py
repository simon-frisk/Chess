import sys
import math
import pygame
import board
import turn
from agents.user import User
from agents.stupid_bot import StupidBot
from pieces.piece import PieceColor

pygame.init()

board = board.Board()
turn = turn.Turn([User(board, PieceColor.WHITE),
                  StupidBot(board, PieceColor.BLACK)])

screen_width = board.BOX_WIDTH * board.BOX_COUNT
display_surface = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Chess')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if type(turn.agent) == User:
                row = math.floor(event.pos[1] / board.BOX_WIDTH)
                column = math.floor(event.pos[0] / board.BOX_WIDTH)
                turn.agent.handle_box_click(row, column, turn.switch_turn)

    if type(turn.agent) == StupidBot:
        turn.agent.handle_turn(turn.switch_turn)

    board.render(display_surface, turn.agent.color)
    turn.agent.render(display_surface, board.BOX_WIDTH)

    pygame.display.update()

    clock.tick(30)
