import pygame
import random
import numpy as np
from board import Board, Token
from ships import create_fleet
from settings import ROWS, COLUMNS, CELL_SIZE, SCREEN_WIDTH


class Gamer:
    """
    Create instance of gamer. Contains attributes:

    :param image: gamer's board
    :type image: Board
    """
    def __init__(self, board: Board):
        self.board = board
        self.fleet = create_fleet()
        self.grid = self.board.grid
        self.logic = self.clean_logic()
        self.turn = False
        self.tokens = []

    def clean_logic(self):
        """
        Set empty logic
        """
        self.logic = self.board.create_game_logic()

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
                size = (ship.h_image.get_width()//CELL_SIZE)
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
    """
    Create instance of player. Contains attributes:

    :param image: player's board
    :type image: Board
    """

    def make_attack(self, grid, logic):
        """
        Function to change board logic
        """
        pos_x, pos_y = pygame.mouse.get_pos()
        if pos_x >= grid[0][0][0] and pos_x <= grid[0][-1][0] + CELL_SIZE and \
           pos_y >= grid[0][0][1] and pos_y <= grid[-1][0][1] + CELL_SIZE:
            for i, row in enumerate(grid):
                for j, col in enumerate(row):
                    if pos_x >= col[0] and pos_x <= col[0] + CELL_SIZE and \
                       pos_y >= col[1] and pos_y <= col[1] + CELL_SIZE:
                        if logic[i][j] == 'H' or logic[i][j] == 'X':
                            print("'Don't repeat shoot in the same place")
                        elif logic[i][j] != ' ' or logic[i][j] == 'O':
                            print("Player hit enemy's ship")
                            logic[i][j] = 'H'
                            self.tokens.append(Token('images/redtoken.png',
                                                     (col)))
                            self.turn = False
                        else:
                            print('Player miss')
                            logic[i][j] = 'X'
                            self.tokens.append(Token('images/bluetoken.png',
                                                     (col)))
                            self.turn = False


class Bot(Gamer):
    """
    Create instance of bot. Contains attributes:

    :param board: bot's board
    :type borad: Board
    """
    def find_target(self, logic: np.ndarray):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if logic[row, col] == 'H':
                    around = []
                    if row - 1 >= 0:
                        up = (row - 1, col)
                        around.append(up)
                    if row + 1 <= ROWS - 1:
                        down = (row + 1, col)
                        around.append(down)
                    if col - 1 >= 0:
                        left = (row, col - 1)
                        around.append(left)
                    if col + 1 <= COLUMNS - 1:
                        right = (row, col + 1)
                        around.append(right)
                    amount = len(around)
                    for element in range(amount):
                        pos = random.choice(around)
                        around.remove(pos)
                        if logic[pos[0], pos[1]] == 'H' or\
                           logic[pos[0], pos[1]] == 'X':
                            continue
                        else:
                            return (pos[0], pos[1])

    def make_attack(self, grid, logic):
        """
        Function to change board logic
        """
        np_logic = np.array(logic)
        valid_choice = False
        if self.find_target(np_logic):
            target = self.find_target(np_logic)
            row = target[0]
            col = target[1]
            valid_choice = True

        while not valid_choice:
            row = random.randint(0, ROWS - 1)
            col = random.randint(0, COLUMNS - 1)
            if logic[row][col] == ' ':
                aroundX = True
                if row - 1 >= 0 and not\
                        (logic[row - 1][col] == 'X'):
                    aroundX = False
                elif row + 1 <= (ROWS - 1) and not\
                        (logic[row + 1][col] == 'X'):
                    aroundX = False
                elif col - 1 >= 0 and not\
                        (logic[row][col - 1] == 'X'):
                    aroundX = False
                elif col + 1 <= (COLUMNS - 1) and not\
                        (logic[row][col + 1] == 'X'):
                    aroundX = False
                valid_choice = not aroundX
            if logic[row][col] == 'O':
                valid_choice = True

        if logic[row][col] == 'O':
            print("Bot hit player's ship")
            logic[row][col] = 'H'
            self.tokens.append(Token('images/redtoken.png', grid[row][col]))
            self.turn = False
        else:
            print('Bot miss')
            logic[row][col] = 'X'
            self.tokens.append(Token('images/bluetoken.png', grid[row][col]))
            self.turn = False


player = Player(Board(ROWS, COLUMNS, CELL_SIZE, (CELL_SIZE, CELL_SIZE)))

bot_grid_position = (SCREEN_WIDTH - (ROWS * CELL_SIZE) - CELL_SIZE, CELL_SIZE)
bot = Bot(Board(ROWS, COLUMNS, CELL_SIZE, bot_grid_position))
