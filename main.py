import pygame
from math import dist
import numpy as np
from settings import (GAME_SCREEN, START_BG, GAME_BG,
                      P_GRID, B_GRID, B_GRID_POS, SHIPS_ZONE,
                      SHIPS_ZONE_POS, PLAYER_WIN, DEFEAT)
from buttons import BUTTONS, deployment_phase_button
from gamers import player, bot
from ships import Ship


def show_game_logic() -> None:
    """
    Show game logic in terminal
    """
    print(' Player Grid '.center(50, '#'))
    for _ in player.logic:
        print(_)
    print(' Bot Grid '.center(50, '#'))
    for _ in bot.logic:
        print(_)


def update_game_screen(window: pygame.surface.Surface) -> None:
    """
    Function to update screen
    """
    window.fill((0, 0, 0))

    if deployment_phase or game_phase:
        # Draw player and bot grids on srceen
        window.blit(GAME_BG, (0, 0))
        window.blit(P_GRID, (0, 0))
        window.blit(B_GRID, B_GRID_POS)
        player.board.show_grid_on_screen(window)
        bot.board.show_grid_on_screen(window)
        # Draw player's ship zone
        if deployment_phase:
            window.blit(SHIPS_ZONE, SHIPS_ZONE_POS)

        # Draw ships on screen
        for ship in player.fleet:
            ship.draw(window)

        # Draw bot's ships on screen
        # for ship in bot.fleet:
        #     ship.draw(window)

    # Draw backgrounds
    elif start_phase:
        window.blit(START_BG, (0, 0))
    elif player_win:
        window.blit(PLAYER_WIN, (0, 0))
    elif player_defeat:
        window.blit(DEFEAT, (0, 0))

    # Draw tokens on the screen
    for token in player.tokens + bot.tokens:
        if game_phase:
            token.draw(window)

    # Draw buttons on the screen
    for button in BUTTONS:
        if deployment_phase and button.name in deployment_phase_button:
            button.draw(window)
        elif (game_phase or end_game) and button.name == 'Menu':
            button.draw(window)
        elif start_phase and button.name == 'Start Game':
            button.draw(window)
        if button.name == 'Quit':
            button.draw(window)
    pygame.display.update()


# Initial player's ships position
def select_ship_and_move(ship: Ship) -> None:
    """
    Select ship and move it to mouse position
    """
    while ship.active is True:
        ship.rect.center = pygame.mouse.get_pos()
        update_game_screen(GAME_SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                ship.align_to_grid_edge(player.grid)
                ship.align_to_grid(player.grid)
                if not ship.check_collision(player.fleet):
                    if event.button == 1:
                        ship.h_image_rect.center = ship.rect.center
                        ship.v_image_rect.center = ship.rect.center
                        ship.active = False
                if event.button == 3:
                    ship.rotate_ship()


dev = False
# change to True,
# if you want use show_game_logic()
# by middle mouse button

# Main Game Loop
if __name__ == "__main__":
    game_run = True
    start_phase = True
    deployment_phase = False
    game_phase = False
    ships_placed = False
    player_win = False
    player_defeat = False
    end_game = False
    while game_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if deployment_phase:
                        for ship in player.fleet:
                            if ship.rect.collidepoint(pygame.mouse.get_pos()):
                                ship.active = True
                                select_ship_and_move(ship)
                    if game_phase:
                        if player.turn:
                            player.make_attack(bot.grid, bot.logic)
                            if not ('O' in np.array(bot.logic)):
                                game_phase = False
                                player_win = True
                                end_game = True
                                # print('Player won')
                            elif not player.turn:
                                bot.turn = True
                        if bot.turn:
                            bot.make_attack(player.grid, player.logic)
                            if not ('O' in np.array(player.logic)):
                                game_phase = False
                                player_defeat = True
                                end_game = True
                                # print('Player defeat')
                            elif not bot.turn:
                                player.turn = True

                    for button in BUTTONS:
                        if button.rect.collidepoint(pygame.mouse.get_pos()):
                            if button.name == "Quit":
                                game_run = False
                            dpb = deployment_phase_button
                            if deployment_phase and button.name in dpb:
                                button.action_on_press()
                            if deployment_phase and button.name == "Deploy":
                                for ship in player.fleet:
                                    if dist(ship.rect.topleft,
                                            ship.position) > 10:
                                        ships_placed = True
                                    else:
                                        ships_placed = False
                                if ships_placed:
                                    deployment_phase = False
                                    game_phase = True
                                    player.turn = True
                                    player.update_game_logic()
                            phase2 = game_phase or end_game
                            if phase2 and button.name == "Menu":
                                start_phase = True
                                game_phase = False
                                player_win = False
                                player_defeat - False
                                end_game = False
                            if start_phase and button.name == "Start Game":
                                player.tokens.clear()
                                bot.tokens.clear()
                                bot.clean_logic()
                                bot.random_ships_placement()
                                bot.update_game_logic()
                                for ship in player.fleet:
                                    ship.return_to_default_potition()
                                player.clean_logic()
                                start_phase = False
                                deployment_phase = True
                # Show game logic in terminal, when middle mouse button clicked
                # and when dev == True
                if dev:
                    if event.button == 2:
                        show_game_logic()

        update_game_screen(GAME_SCREEN)

    pygame.quit()
