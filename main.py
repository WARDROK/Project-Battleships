from ships import create_fleet
from grid import create_game_grid, update_game_logic, show_grid_on_screen
import pygame
pygame.init()


# Settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 900
ROWS = 10
COLUMNS = 10
CELL_SIZE = 50


# Display Initialization
GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Battleships')


# Variables
player_grid = create_game_grid(ROWS, COLUMNS, CELL_SIZE, (50, 50))
player_logic = update_game_logic(ROWS, COLUMNS)
player_fleet = create_fleet()

bot_grid = create_game_grid(ROWS, COLUMNS, CELL_SIZE, (SCREEN_WIDTH - (ROWS * CELL_SIZE) - CELL_SIZE, 50))
bot_logic = update_game_logic(ROWS, COLUMNS)
bot_fleet = None


# Screen update function
def update_game_screen(window):
    """
    Function to update screen
    """
    window.fill((0, 0, 0))

    # Draw player and bot grids on srceen
    show_grid_on_screen(window, CELL_SIZE, player_grid, bot_grid)

    # Draw ships on screen
    for ship in player_fleet:
        ship.draw(window)

    pygame.display.update()


# Main Game Loop
game_run = True
while game_run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    update_game_screen(GAME_SCREEN)

pygame.quit()
