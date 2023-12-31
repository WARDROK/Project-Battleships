import pygame
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

    # Draw player and bot grids on srceen
    player.board.show_grid_on_screen(window)
    bot.board.show_grid_on_screen(window)

    # Draw ships on screen
    for ship in player.fleet:
        ship.draw(window)

    # Draw bot's ships on screen
    for ship in bot.fleet:
        ship.draw(window)

    # Draw buttons on the screen
    for button in BUTTONS:
        if deployment_phase and button.name in deployment_phase_button:
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
    deployment_phase = True
    game_phase = False
    next_phase = False
    ships_placed = False
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
                            if not player.turn:
                                bot.turn = True
                        if bot.turn:
                            bot.make_attack(player.grid, player.logic)
                            if not bot.turn:
                                player.turn = True

                    for button in BUTTONS:
                        if button.rect.collidepoint(pygame.mouse.get_pos()):
                            dpb = deployment_phase_button
                            if deployment_phase and button.name in dpb:
                                button.action_on_press()
                            if button.name == "Deploy":
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
                if event.button == 2:
                    show_game_logic()

        update_game_screen(GAME_SCREEN)

    pygame.quit()
