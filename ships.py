import pygame


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
        # Vertical image
        self.name = name
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

    def draw(self, window):
        """
        Draw ship on screen
        """
        window.blit(self.image, self.rect)
