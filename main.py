import sys
import pygame
import board

pygame.init()

board = board.Board()

screen_width = board.BOX_WIDTH * board.BOX_COUNT
display_surface = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Chess')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    board.render(display_surface)

    pygame.display.update()

    clock.tick(30)
