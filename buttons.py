import pygame
from settings import load_image, scale, SCREEN_HEIGHT, SCREEN_WIDTH
from gamers import Player, player
from typing import Tuple, List


class Button:
    """
    Create instance of button. Contains attributes:

    :param image: button's image surface
    :type image: pygame.surface.Surface

    :param size: button's size (x, y)
    :type size: tuple

    :param pos: button's pos (x, y)
    :type pos: tuple

    :param msg: button's message
    :type msg: str
    """
    def __init__(self, image: pygame.surface.Surface,
                 size: Tuple[float, float],
                 pos: Tuple[float, float],
                 msg: str, center: bool = False) -> None:
        self.center = center
        self.name = msg
        self.image = image
        data1 = scale(size[0]), scale(size[1])
        transform = pygame.transform.scale(image, data1)
        data2 = scale(size[0] + 10), scale(size[1] + 10)
        transform_large = pygame.transform.scale(image, data2)
        self.image = transform
        self.image_larger = transform_large
        self.rect = self.image.get_rect()
        self.rect.topleft = (scale(pos[0]), scale(pos[1]))
        if center:
            self.rect.topleft = ((SCREEN_WIDTH - scale(size[0]))//2,
                                 (SCREEN_HEIGHT - scale(size[1]))//2)
        self.active = False
        self.msg = self.add_text(msg)
        self.msg_rect = self.msg.get_rect(center=self.rect.center)

    def add_text(self, msg: str) -> pygame.surface.Surface:
        """
        Add text to button
        """
        if self.center:
            font = pygame.font.SysFont('Sans', round(scale(36)))
        else:
            font = pygame.font.SysFont('Sans', round(scale(24)))
        return font.render(msg, 1, (255, 255, 255))

    def focus_on_button(self, window: pygame.surface.Surface) -> None:
        """
        Larger image when mouse focus on button
        """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_larger, (self.rect[0] - scale(5),
                                            self.rect[1] - scale(5),
                                            self.rect[2], self.rect[3]))
        else:
            window.blit(self.image, self.rect)

    def action_on_press(self) -> None:
        """
        Make button actions when clicked
        """
        if self.name == 'Randomize':
            self.randomize(player)
        elif self.name == 'Reset':
            self.reset(player.fleet)

    def randomize(self, player: Player) -> None:
        """
        Call random ship placement fucntion
        """
        player.random_ships_placement()

    def reset(self, ship_list: List[object]) -> None:
        """
        Set ships on default positions
        """
        for ship in ship_list:
            ship.return_to_default_potition()

    def draw(self, window: pygame.surface.Surface) -> None:
        """
        Draw button on screen
        """
        self.focus_on_button(window)
        window.blit(self.msg, self.msg_rect)


if __name__ == 'buttons':
    BUTTON_IMAGE = load_image('images/button.png', (scale(150), scale(75)))
    BUTTONS = [
        Button(BUTTON_IMAGE, (150, 75), (25, 900), 'Randomize'),
        Button(BUTTON_IMAGE, (150, 75), (200, 900), 'Reset'),
        Button(BUTTON_IMAGE, (150, 75), (375, 900), 'Deploy'),
        Button(BUTTON_IMAGE, (150, 75), (25, 900), 'Menu'),
        Button(BUTTON_IMAGE, (150, 75), (1745, 900), 'Quit'),
        Button(BUTTON_IMAGE, (300, 100), (0, 0), 'Start Game', center=True)
    ]

    deployment_phase_button = ['Randomize', 'Reset', 'Deploy']
