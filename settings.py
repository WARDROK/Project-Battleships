import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1000
ROWS = 10
COLUMNS = 10
CELL_SIZE = 50

pygame.init()
GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Battleships')
