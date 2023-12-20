import pygame
from settings import (
    CELL_SIZE,
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


def create_fleet():
    """
    Create fleet of ships
    """
    fleet = []
    for name in FLEET.keys():
        fleet.append(
            Ship(name,
                 FLEET[name][1],
                 FLEET[name][2],
                 FLEET[name][3])
        )
    return fleet


FLEET = {
    'carrier': ['carrier', 'images/carrier.png',
                (50, 600), (45, 245)],
    'battleship': ['battleship', 'images/battleship.png',
                   (125, 600), (30, 195)],
    'cruiser': ['cruiser', 'images/cruiser.png',
                (200, 600), (30, 145)],
    'destroyer': ['destroyer', 'images/destroyer.png',
                  (275, 600), (30, 145)],
    'submarine': ['submarine', 'images/submarine.png',
                  (350, 600), (20, 95)],
}


class Ship:
    """
    Create instance of ship. Contains attributes:

    :param name: ships's name
    :type name: str

    :param image: ships's image path
    :type image: str

    :param position: ships's starting coordinates (x,y)
    :type position: tuple

    :param size: ships's size (x, y)
    :type position: tuple
    """
    def __init__(self, name: str, image: str, position: tuple, size: tuple):
        self.name = name
        self.position = position
        # Vertical image
        self.v_image = load_image(image, size)
        self.v_image_width = self.v_image.get_width()
        self.v_image_height = self.v_image.get_height()
        self.v_image_rect = self.v_image.get_rect()
        self.v_image_rect.topleft = position
        # Horizontal image
        self.h_image = pygame.transform.rotate(self.v_image, -90)
        self.h_image_width = self.h_image.get_width()
        self.h_image_height = self.h_image.get_height()
        self.h_image_rect = self.h_image.get_rect()
        self.h_image_rect.topleft = position
        # Image and Rectangle
        self.image = self.v_image
        self.rect = self.v_image_rect
        self.rotation = False
        # Ship is active select
        self.active = False

    def rotate_ship(self):
        """
        Switch ship rotation(wertical or horizontal)
        """
        pass

    def draw(self, window):
        """
        Draw ship on screen
        """
        window.blit(self.image, self.rect)

    def check_collision(self, ship_list: list):
        """
        Check if ship is colliding with others ships
        """
        copy = ship_list.copy()
        copy.remove(self)
        for item in copy:
            if self.rect.colliderect(item.rect):
                return True
        return False

    def return_to_default_potition(self):
        """
        Return ship to default position
        """
        self.rect.topleft = self.position
        self.h_image_rect = self.rect.center
        self.v_image_rect = self.rect.center

    def align_to_grid_edge(self, grid_coords):
        if self.rect.topleft != self.position:

            # Check if ship out of game grid
            if self.rect.left > grid_coords[0][-1][0] + CELL_SIZE or \
               self.rect.right < grid_coords[0][0][0] or \
               self.rect.top > grid_coords[-1][0][1] + CELL_SIZE or \
               self.rect.bottom < grid_coords[0][0][1]:
                self.return_to_default_potition()

            elif self.rect.right > grid_coords[0][-1][0] + CELL_SIZE:
                self.rect.right = grid_coords[0][-1][0] + CELL_SIZE
            elif self.rect.left < grid_coords[0][0][0]:
                self.rect.left = grid_coords[0][0][0]
            elif self.rect.top < grid_coords[0][0][1]:
                self.rect.top = grid_coords[0][0][1]
            elif self.rect.bottom > grid_coords[-1][0][1] + CELL_SIZE:
                self.rect.bottom = grid_coords[-1][0][1] + CELL_SIZE
            self.h_image_rect = self.rect.center
            self.v_image_rect = self.rect.center

    def align_to_edge(self, grid_coords):
        for row in grid_coords:
            for cell in row:
                if self.rect.left >= cell[0] and \
                   self.rect.left < cell[0] + CELL_SIZE and \
                   self.rect.top >= cell[1] and \
                   self.rect.top < cell[1] + CELL_SIZE:
                    self.rect.topleft = (cell[0] + ((CELL_SIZE - self.image.get_width())//2), cell[1])  # edytować wysokość wstaiwania statków
        self.h_image_rect = self.rect.center
        self.v_image_rect = self.rect.center
