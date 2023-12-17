import pygame


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


def show_grid_on_screen(window, cell_size, player_grid, bot_grid):
    """
    Show player and bot grids on screen
    """
    game_grids = [player_grid, bot_grid]
    for grid in game_grids:
        for row in grid:
            for column in row:
                pygame.draw.rect(window, (255, 255, 255), (column[0], column[1], cell_size, cell_size), 1)
