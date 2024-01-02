import pygame
from settings import CELL_SIZE, load_image, scale


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
                (scale(50), scale(600)), (scale(45), scale(245))],
    'battleship': ['battleship', 'images/battleship.png',
                   (scale(125), scale(600)), (scale(30), scale(195))],
    'cruiser': ['cruiser', 'images/cruiser.png',
                (scale(200), scale(600)), (scale(30), scale(145))],
    'destroyer': ['destroyer', 'images/destroyer.png',
                  (scale(275), scale(600)), (scale(30), scale(145))],
    'submarine': ['submarine', 'images/submarine.png',
                  (scale(350), scale(600)), (scale(30), scale(95))],
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
    :type size: tuple
    """
    def __init__(self, name, image, position, size):
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

    def set_center_point():
        """
        Set ships's center point
        """
        pass

    def rotate_ship(self):
        """
        Change ship rotation(vertical or horizontal)
        """
        if self.rotation is False:
            self.rotation = True
        else:
            self.rotation = False
        self.rotate_image()

    def rotate_image(self):
        """
        Change image (vertical or horizontal)
        """
        if self.rotation is True:
            self.image = self.h_image
            self.rect = self.h_image_rect
        else:
            self.image = self.v_image
            self.rect = self.v_image_rect
        self.h_image_rect.center = self.rect.center
        self.v_image_rect.center = self.rect.center

    def draw(self, window):
        """
        Draw ship on screen
        """
        window.blit(self.image, self.rect)

        # red line around ships
        # pygame.draw.rect(window, (255, 0, 0), self.rect, 1)

    def check_collision(self, ship_list):
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
        if self.rotation is True:
            self.rotate_ship()
        self.rect.topleft = self.position
        self.h_image_rect.center = self.rect.center
        self.v_image_rect.center = self.rect.center

    def align_to_grid_edge(self, grid_coords):
        """
        Adjust ship position to the game grid edge
        """
        if self.rect.topleft != self.position and self.active is True:

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
            self.h_image_rect.center = self.rect.center
            self.v_image_rect.center = self.rect.center

            if self.rect.bottom > grid_coords[-1][0][1] + CELL_SIZE or \
               self.rect.top < grid_coords[0][0][1] - CELL_SIZE:
                self.return_to_default_potition()

    def align_to_grid(self, grid_coords):
        """
        Adjust ship position to the game grid
        """
        correct_width = (CELL_SIZE - self.image.get_width())//2
        correct_height = (CELL_SIZE - self.image.get_height())//2
        for row in grid_coords:
            for cell in row:
                if self.rect.left >= cell[0] - CELL_SIZE//2 and \
                   self.rect.left < cell[0] + CELL_SIZE//2 and \
                   self.rect.top >= cell[1] - CELL_SIZE//2 and \
                   self.rect.top < cell[1] + CELL_SIZE//2:
                    if self.rotation is False:
                        self.rect.topleft = (cell[0] + correct_width, cell[1])
                    else:
                        self.rect.topleft = (cell[0], cell[1] + correct_height)
        self.h_image_rect.center = self.rect.center
        self.v_image_rect.center = self.rect.center
