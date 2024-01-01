import pygame
import numpy as np
from settings import GAME_SCREEN
from buttons import BUTTONS, deployment_phase_button
from gamers import player, bot


def show_game_logic():
    """
    Show game logic in terminal
    """
    print(' Player Grid '.center(50, '#'))
    for _ in player.logic:
        print(_)
    print(' Bot Grid '.center(50, '#'))
    for _ in bot.logic:
        print(_)


# Screen update function
def update_game_screen(window):
    """
    Function to update screen
    """
    window.fill((0, 0, 0))

    if deployment_phase or game_phase:
        # Draw player and bot grids on srceen
        player.board.show_grid_on_screen(window)
        bot.board.show_grid_on_screen(window)

        # Draw ships on screen
        for ship in player.fleet:
            ship.draw(window)

        # Draw bot's ships on screen
        # for ship in bot.fleet:
        #     ship.draw(window)

    elif start_phase:
        pass

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
                ship.align_to_grid_edge(player.grid)
                ship.align_to_grid(player.grid)
                if not ship.check_collision(player.fleet):
                    if event.button == 1:
                        ship.h_image_rect.center = ship.rect.center
                        ship.v_image_rect.center = ship.rect.center
                        ship.active = False
                if event.button == 3:
                    ship.rotate_ship()


# Main Game Loop
if __name__ == "__main__":
    bot.random_ships_placement()
    bot.update_game_logic()
    game_run = True
    start_phase = False
    deployment_phase = True
    game_phase = False
    ships_placed = False
    player_win = False
    player_defeat = False
    end_game = False
    while game_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            # Only after start game and before deploy
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
                                print('Player won')
                            if not player.turn:
                                bot.turn = True
                        if bot.turn:
                            bot.make_attack(player.grid, player.logic)
                            if not ('O' in np.array(player.logic)):
                                game_phase = False
                                player_defeat = True
                                end_game = True
                                print('Player defeat')
                            if not bot.turn:
                                player.turn = True

                    for button in BUTTONS:
                        if button.rect.collidepoint(pygame.mouse.get_pos()):
                            dpb = deployment_phase_button
                            if deployment_phase and button.name in dpb:
                                button.action_on_press()
                            if deployment_phase and button.name == "Deploy":
                                for ship in player.fleet:
                                    if ship.rect.topleft != ship.position:
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
                if event.button == 2:
                    show_game_logic()

        update_game_screen(GAME_SCREEN)

    pygame.quit()
