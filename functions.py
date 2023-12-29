import pygame
import random
from settings import (
    ROWS,
    COLUMNS,
)


def load_image(path, size, roatate=False):
    """
    Function to import images
    """
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, size)
    if roatate is True:
        img = pygame.transform.rotate(img, -90)
    return img


def random_ships_placement(ship_list, game_grid):
    """
    Random locate ships on the game grid
    """
    placed_ships = []
    for ship in ship_list:
        valid_position = False
        while not valid_position:
            ship.return_to_default_potition()
            rotate_ship = random.choice([True, False])
            size = (ship.h_image.get_width()//50)
            if rotate_ship is True:
                ship.rotate_ship()
                y = random.randint(0, ROWS - size)
                x = random.randint(0, COLUMNS - size - 1)
                ship.rect.topleft = game_grid[y][x]
            else:
                y = random.randint(0, ROWS - size - 1)
                x = random.randint(0, COLUMNS - size)
                ship.rect.topleft = game_grid[y][x]
            if len(placed_ships) > 0:
                for item in placed_ships:
                    if ship.rect.colliderect(item.rect):
                        valid_position = False
                        break
                    else:
                        valid_position = True
            else:
                valid_position = True
            ship.align_to_grid(game_grid)
            ship.align_to_grid_edge(game_grid)
        placed_ships.append(ship)
