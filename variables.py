from ships import create_fleet
from board import Board
from settings import (
    SCREEN_WIDTH,
    ROWS,
    COLUMNS,
    CELL_SIZE,
)

player_board = Board(ROWS, COLUMNS, CELL_SIZE, (50, 50))
player_grid = player_board.create_game_grid()
player_logic = player_board.create_game_logic()
player_fleet = create_fleet()

bot_grid_position = (SCREEN_WIDTH - (ROWS * CELL_SIZE) - CELL_SIZE, 50)
bot_board = Board(ROWS, COLUMNS, CELL_SIZE, bot_grid_position)
bot_grid = bot_board.create_game_grid()
bot_logic = bot_board.create_game_logic()
bot_fleet = create_fleet()
