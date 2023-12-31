import pygame

CELL_SIZE = 40  # 50 optimal
SCREEN_WIDTH = 1280/50*CELL_SIZE
SCREEN_HEIGHT = 1000/50*CELL_SIZE
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
    return number/50*CELL_SIZE
