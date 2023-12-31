import pygame
from settings import CELL_SIZE, load_image


class Board:
    """
    Create instance of Board. Contains attributes:

    :param rows: board's rows
    :type rows: int

    :param columns: board's columns
    :type columns: int

    :param cell_size: boards's cell size
    :type cell_size: int

    :param size: boards's starting coordinates (x, y)
    :type position: tuple
    """

    def __init__(self, rows: int, columns: int,
                 cell_size: int, position: tuple):
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.position = position
        self.grid = self.create_grid()
        self.logic = self.create_game_logic()

    def create_grid(self):
        """
        Create a game grid
        """
        start_x = self.position[0]
        start_y = self.position[1]
        grid = []
        for row in range(self.rows):
            row_x = []
            for column in range(self.columns):
                row_x.append((start_x, start_y))
                start_x += self.cell_size
            grid.append(row_x)
            start_x = self.position[0]
            start_y += self.cell_size
        return grid

    def create_game_logic(self):
        """
        Create game grid with logic
        ' ' - spaces
        'O' - ships
        'H' - hitted
        'X' - missed
        """
        game_logic = []
        for row in range(self.rows):
            row_x = []
            for column in range(self.columns):
                row_x .append(' ')
            game_logic.append(row_x)
        return game_logic

    def show_grid_on_screen(self, window):
        """
        Show player and bot grids on screen
        """
        grid = self.grid
        for row in grid:
            for column in row:
                rect = (column[0], column[1], self.cell_size, self.cell_size)
                pygame.draw.rect(window, (255, 255, 255), rect, 1)


class Token:
    """
    Create instance of Token. Contains attributes:

    :param image: token's image
    :type image: str

    :param pos: token's position
    :type pos: tuple
    """
    def __init__(self, image: str, pos: tuple) -> None:
        self.image = load_image(image, (CELL_SIZE, CELL_SIZE))
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def draw(self, window):
        """
        Draw token on screen
        """
        window.blit(self.image, self.rect)
