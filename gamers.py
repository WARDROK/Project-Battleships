import pygame
import random
from board import Board
from ships import create_fleet
from settings import ROWS, COLUMNS, CELL_SIZE, SCREEN_WIDTH


class Gamer:
    def __init__(self, board: Board):
        self.board = board
        self.fleet = create_fleet()
        self.grid = self.board.grid
        self.logic = self.board.logic

    def random_ships_placement(self):
        """
        Random locate ships on the game grid
        """
        placed_ships = []
        for ship in self.fleet:
            valid_position = False
            while not valid_position:
                ship.return_to_default_potition()
                rotate_ship = random.choice([True, False])
                size = (ship.h_image.get_width()//50)
                if rotate_ship is True:
                    ship.rotate_ship()
                    y = random.randint(0, ROWS - size)
                    x = random.randint(0, COLUMNS - size - 1)
                    ship.rect.topleft = self.grid[y][x]
                else:
                    y = random.randint(0, ROWS - size - 1)
                    x = random.randint(0, COLUMNS - size)
                    ship.rect.topleft = self.grid[y][x]
                if len(placed_ships) > 0:
                    for item in placed_ships:
                        if ship.rect.colliderect(item.rect):
                            valid_position = False
                            break
                        else:
                            valid_position = True
                else:
                    valid_position = True
                ship.align_to_grid(self.grid)
                ship.align_to_grid_edge(self.grid)
            placed_ships.append(ship)

    def update_game_logic(self):
        """
        Update game grid with position of the ships
        """
        grid_coords = self.grid
        game_logic = self.logic
        for i, row in enumerate(grid_coords):
            for j, col in enumerate(row):
                if game_logic[i][j] == 'H' or game_logic[i][j] == 'X':
                    continue
                else:
                    game_logic[i][j] = ' '
                    for ship in self.fleet:
                        data = col[0], col[1], CELL_SIZE, CELL_SIZE
                        if pygame.rect.Rect(data).colliderect(ship.rect):
                            game_logic[i][j] = "O"


class Player(Gamer):
    def __init__(self, board: Board):
        super().__init__(board)


class Bot(Gamer):
    def __init__(self, board: Board):
        super().__init__(board)


player = Player(Board(ROWS, COLUMNS, CELL_SIZE, (50, 50)))

bot_grid_position = (SCREEN_WIDTH - (ROWS * CELL_SIZE) - CELL_SIZE, 50)
bot = Bot(Board(ROWS, COLUMNS, CELL_SIZE, bot_grid_position))
