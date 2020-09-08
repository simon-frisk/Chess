import sys
import math
import pygame
import board
from agents.user import User
from agents.stupid_bot import StupidBot
from pieces.piece import PieceColor

pygame.init()

board = board.Board()
agents = (User(board, PieceColor.WHITE), StupidBot(board, PieceColor.BLACK))
current_turn_agent = agents[0]

screen_width = board.BOX_WIDTH * board.BOX_COUNT
display_surface = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Chess')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        if(event.type == pygame.MOUSEBUTTONDOWN):
            row = math.floor(event.pos[1] / board.BOX_WIDTH)
            column = math.floor(event.pos[0] / board.BOX_WIDTH)
            current_turn_agent.handle_box_click(row, column)

    board.render(display_surface)
    current_turn_agent.render(display_surface, board.BOX_WIDTH)

    pygame.display.update()

    clock.tick(30)
