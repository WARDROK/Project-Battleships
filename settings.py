import pygame
from errors import (LowWidthResolution, LowHeightResolution,
                    WrongResolutionData, NotFile)

try:
    with open('screen_resolution.txt')as fh:
        width = fh.readline()
        height = fh.readline()
        screen_width = int(width[13::])
        screen_height = int(height[14::])
        if screen_width < 800:
            raise LowWidthResolution(screen_width)
        if screen_height < 600:
            raise LowHeightResolution(screen_height)
except ValueError:
    raise WrongResolutionData()
except FileNotFoundError:
    with open('screen_resolution.txt', 'w') as fh:
        fh.write('screen_width=1280\nscreen_height=720')
    raise NotFile()


CELL_SIZE = 50*screen_height/1080
SCREEN_WIDTH = screen_width
SCREEN_HEIGHT = screen_height
ROWS = 10
COLUMNS = 10

pygame.init()
GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Battleships')


def load_image(path, size, roatate=False):
    """
    Function to import images
    """
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, size)
    if roatate is True:
        img = pygame.transform.rotate(img, -90)
    return img


def scale(number):
    """
    Function to make scale based on CELL_SIZE
    """
    return number/50*CELL_SIZE


START_BG = load_image('images/start_bg.jpg', (SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_BG = load_image('images/game_bg.png', (SCREEN_WIDTH, SCREEN_HEIGHT))
P_GRID = load_image('images/player_grid.png', (CELL_SIZE*11, CELL_SIZE*11))
B_GRID = load_image('images/bot_grid.png', (CELL_SIZE*11, CELL_SIZE*11))
B_GRID_POS = (SCREEN_WIDTH - (ROWS * CELL_SIZE) - CELL_SIZE, 0)
SHIPS_ZONE = load_image('images/ships_zone.png', (CELL_SIZE*11, CELL_SIZE*5))
SHIPS_ZONE_POS = (0, CELL_SIZE*12)
PLAYER_WIN = load_image('images/player_win.jpg', (SCREEN_WIDTH, SCREEN_HEIGHT))
DEFEAT = load_image('images/defeat.jpg', (SCREEN_WIDTH, SCREEN_HEIGHT))
