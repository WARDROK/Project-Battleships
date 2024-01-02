import pygame

CELL_SIZE = 50  # 50 optimal
SCREEN_WIDTH = 1600/50*CELL_SIZE
SCREEN_HEIGHT = 980/50*CELL_SIZE
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
