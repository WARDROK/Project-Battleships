from board import Board
from buttons import Button
from ships import create_fleet
from functions import load_image, random_ships_placement
from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ROWS,
    COLUMNS,
    CELL_SIZE,
)

import pygame
pygame.init()


# Display amd Board Initialization
GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Battleships')
BUTTON_IMAGE = load_image('images/button.png', (150, 50))

BUTTONS = [
    Button(BUTTON_IMAGE, (150, 50), (25, 900), 'Randomize')
]


# Variables
player_board = Board(ROWS, COLUMNS, CELL_SIZE, (50, 50))
player_grid = player_board.create_game_grid()
player_logic = player_board.update_game_logic()
player_fleet = create_fleet()

bot_grid_position = (SCREEN_WIDTH - (ROWS * CELL_SIZE) - CELL_SIZE, 50)
bot_board = Board(ROWS, COLUMNS, CELL_SIZE, bot_grid_position)
bot_grid = bot_board.create_game_grid()
bot_logic = bot_board.update_game_logic()
bot_fleet = create_fleet()


def show_game_logic():
    """
    Show game logic in terminal
    """
    print(' Player Grid '.center(50, '#'))
    for _ in player_logic:
        print(_)
    print(' Bot Grid '.center(50, '#'))
    for _ in bot_logic:
        print(_)


# Screen update function
def update_game_screen(window):
    """
    Function to update screen
    """
    window.fill((0, 0, 0))

    # Draw player and bot grids on srceen
    player_board.show_grid_on_screen(window)
    bot_board.show_grid_on_screen(window)

    # Draw ships on screen
    for ship in player_fleet:
        ship.draw(window)

    # Draw bot's ships on screen
    for ship in bot_fleet:
        ship.draw(window)

    # Draw buttons on the screen
    for button in BUTTONS:
        button.draw(window)

    pygame.display.update()


# Initial player's ships position
def select_ship_and_move(ship):
    """
    Select ship and move it to mouse position
    """
    while ship.active is True:
        ship.rect.center = pygame.mouse.get_pos()
        update_game_screen(GAME_SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                ship.align_to_grid_edge(player_grid)
                ship.align_to_grid(player_grid)
                if not ship.check_collision(player_fleet):
                    if event.button == 1:
                        ship.h_image_rect.center = ship.rect.center
                        ship.v_image_rect.center = ship.rect.center
                        ship.active = False
                if event.button == 3:
                    ship.rotate_ship()


# Main Game Loop
if __name__ == "__main__":
    random_ships_placement(bot_fleet, bot_grid)
    show_game_logic()
    game_run = True
    while game_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            # Only after start game and before deploy
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for ship in player_fleet:
                        if ship.rect.collidepoint(pygame.mouse.get_pos()):
                            ship.active = True
                            select_ship_and_move(ship)

        update_game_screen(GAME_SCREEN)

    pygame.quit()
