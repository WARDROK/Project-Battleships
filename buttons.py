import pygame
from functions import random_ships_placement


class Button:
    """
    Create instance of button. Contains attributes:

    :param image: button's image path
    :type image: str

    :param size: button's size (x, y)
    :type size: tuple

    :param pos: button's pos (x, y)
    :type pos: tuple

    :param msg: button's message
    :type msg: str


    """
    def __init__(self, image, size, pos, msg):
        self.name = msg
        self.image = image
        scale = pygame.transform.scale(image, (size[0] + 10, size[1] + 10))
        self.image_larger = scale
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.active = False
        self.msg = self.add_text(msg)
        self.msg_rect = self.msg.get_rect(center=self.rect.center)

    def add_text(self, msg):
        """
        Add text to button
        """
        font = pygame.font.SysFont('Stencil', 36)
        return font.render(msg, 1, (255, 255, 255))

    def focus_on_button(self, window):
        """
        Larger image when mouse focus on button
        """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_larger, (self.rect[0] - 5, self.rect[1] - 5,
                                            self.rect[2], self.rect[3]))
        else:
            window.blit(self.image, self.rect)

    def action_on_press(self):
        """
        Make button actions when clicked
        """
        if self.name == "Randomize":
            self.randomize()

    def randomize(self, ship_list, game_grid):
        """
        Call random ship placement fucntion
        """
        random_ships_placement(ship_list, game_grid)

    def draw(self, window):
        self.focus_on_button(window)
        window.blit(self.msg, self.msg_rect)
