from board import Board
from ships import create_fleet
from settings import ROWS, COLUMNS, CELL_SIZE, SCREEN_WIDTH


class Gamer:
    def __init__(self, board: Board):
        self.board = board
        self.fleet = create_fleet()
        self.grid = self.board.grid
        self.logic = self.board.create_game_logic()


class Player(Gamer):
    def __init__(self, board: Board):
        super().__init__(board)


class Bot(Gamer):
    def __init__(self, board: Board):
        super().__init__(board)


player = Player(Board(ROWS, COLUMNS, CELL_SIZE, (50, 50)))

bot_grid_position = (SCREEN_WIDTH - (ROWS * CELL_SIZE) - CELL_SIZE, 50)
bot = Bot(Board(ROWS, COLUMNS, CELL_SIZE, bot_grid_position))
