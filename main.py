# Module
import pygame
pygame.init()


# Game Utilities
def create_game_grid(rows: int, columns: int, cell_size: int, position: tuple):
    """
    Create a game grid
    """
    start_x = position[0]
    start_y = position[1]
    grid_coordinations = []
    for row in range(rows):
        row_x = []
        for column in range(columns):
            row_x.append((start_x, start_y))
            start_x += cell_size
        grid_coordinations.append(row_x)
        start_x = position[0]
        start_y += cell_size
    return grid_coordinations


def update_game_logic(rows: int, columns: int):
    """
    Update game grid with logic, - spaces, X ships
    """
    game_logic = []
    for row in range(rows):
        row_x = []
        for column in range(columns):
            row_x .append(' ')
        game_logic.append(row_x)
    return game_logic


def show_game_logic() -> None:
    """
    Show game logic in terminal
    """
    print('Player Grid'.center(50, '#'))
    for _ in player_logic:
        print(_)
    print('Bot Grid'.center(50, '#'))
    for _ in bot_logic:
        print(_)


def show_grid_on_screen(window, cell_size, player_grid, bot_grid):
    """
    Show player and bot grids on screen
    """
    game_grids = [player_grid, bot_grid]
    for grid in game_grids:
        for row in grid:
            for column in row:
                pygame.draw.rect(window, (255, 255, 255), (column[0], column[1], cell_size, cell_size), 1)


def load_image(path, size, roatate=False):
    """
    Function to import images
    """
    img = pygame.image.load(path).convert.alpha()
    img = pygame.transform.scale(img, size)
    if roatate is True:
        img = pygame.transform.rotate(img, -90)
    return img


def update_game_screen(window):
    """
    Draw player and bot grids on srceen
    """
    window.fill((0, 0, 0))
    show_grid_on_screen(window, CELL_SIZE, player_grid, bot_grid)

    pygame.display.update()


# Settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
ROWS = 10
COLUMNS = 10
CELL_SIZE = 50


# Display Initialization
GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Battleships')


# Variables
player_grid = create_game_grid(ROWS, COLUMNS, CELL_SIZE, (50, 50))
player_logic = update_game_logic(ROWS, COLUMNS)

bot_grid = create_game_grid(ROWS, COLUMNS, CELL_SIZE, (SCREEN_WIDTH - (ROWS * CELL_SIZE) - CELL_SIZE, 50))
bot_logic = update_game_logic(ROWS, COLUMNS)


# Main Game Loop
game_run = True
while game_run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    update_game_screen(GAME_SCREEN)

pygame.quit()
