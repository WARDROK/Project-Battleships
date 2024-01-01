import pygame
from settings import load_image, scale
from gamers import player


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
        data = scale(size[0] + 10), scale(size[1] + 10)
        transform = pygame.transform.scale(image, data)
        self.image_larger = transform
        self.rect = self.image.get_rect()
        self.rect.topleft = (scale(pos[0]), scale(pos[1]))
        self.active = False
        self.msg = self.add_text(msg)
        self.msg_rect = self.msg.get_rect(center=self.rect.center)

    def add_text(self, msg):
        """
        Add text to button
        """
        font = pygame.font.SysFont('Stencil', round(scale(36)))
        return font.render(msg, 1, (255, 255, 255))

    def focus_on_button(self, window):
        """
        Larger image when mouse focus on button
        """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_larger, (self.rect[0] - scale(5),
                                            self.rect[1] - scale(5),
                                            self.rect[2], self.rect[3]))
        else:
            window.blit(self.image, self.rect)

    def action_on_press(self):
        """
        Make button actions when clicked
        """
        if self.name == 'Randomize':
            self.randomize(player)
        elif self.name == 'Reset':
            self.reset(player.fleet)

    def randomize(self, player):
        """
        Call random ship placement fucntion
        """
        player.random_ships_placement()

    def reset(self, ship_list):
        """
        Set ships on default positions
        """
        for ship in ship_list:
            ship.return_to_default_potition()

    def draw(self, window):
        self.focus_on_button(window)
        window.blit(self.msg, self.msg_rect)


BUTTON_IMAGE = load_image('images/button.png', (scale(150), scale(50)))
BUTTONS = [
    Button(BUTTON_IMAGE, (150, 50), (25, 900), 'Randomize'),
    Button(BUTTON_IMAGE, (150, 50), (200, 900), 'Reset'),
    Button(BUTTON_IMAGE, (150, 50), (375, 900), 'Deploy'),
    Button(BUTTON_IMAGE, (150, 50), (25, 900), 'Menu'),

]

deployment_phase_button = ['Randomize', 'Reset', 'Deploy']
menu_button = ['Menu']
