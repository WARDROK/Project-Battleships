import pygame
from errors import (LowWidthResolution, LowHeightResolution,
                    WrongResolutionData, NotFile)


def set_default_resolution(screen_width: str = '1280',
                           screen_height: str = '720') -> None:
    """
    Set default resolution
    """
    with open('screen_resolution.txt', 'w') as fh:
        fh.write(f'screen_width={screen_width}\nscreen_height={screen_height}')


def read_resolution(screen_width: str = None,
                    screen_height: str = None,
                    file: str = None) -> tuple[str, str]:
    """
    Read resolution from file[default: 'screen_resolution.txt']
    """
    if file is None:
        file = 'screen_resolution.txt'
    try:
        with open(file) as fh:
            if screen_width is None:
                screen_width = fh.readline()
            screen_width = int(screen_width[13::])
            if screen_height is None:
                screen_height = fh.readline()
            screen_height = int(screen_height[14::])
            if screen_width < 800:
                set_default_resolution()
                raise LowWidthResolution(screen_width)
            if screen_height < 600:
                set_default_resolution()
                raise LowHeightResolution(screen_height)
    except ValueError:
        set_default_resolution()
        raise WrongResolutionData()
    except FileNotFoundError:
        set_default_resolution()
        raise NotFile()
    return (screen_width, screen_height)


if __name__ == 'settings':
    res = read_resolution()
    CELL_SIZE = 50*res[1]/1080
    SCREEN_WIDTH = res[0]
    SCREEN_HEIGHT = res[1]
    ROWS = 10
    COLUMNS = ROWS

    pygame.init()
    GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Battleships')

    def load_image(path: str,
                   size: tuple[float, float],
                   roatate=False) -> pygame.surface.Surface:
        """
        Function to import images
        """
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, size)
        if roatate is True:
            img = pygame.transform.rotate(img, -90)
        return img

    def scale(number: float) -> float:
        """
        Function to make scale based on CELL_SIZE
        """
        return number/50*CELL_SIZE

    START_BG = load_image('images/start_bg.jpg', (SCREEN_WIDTH, SCREEN_HEIGHT))
    GAME_BG = load_image('images/game_bg.png', (SCREEN_WIDTH, SCREEN_HEIGHT))
    P_GRID = load_image('images/player_grid.png', (CELL_SIZE*11, CELL_SIZE*11))
    B_GRID = load_image('images/bot_grid.png', (CELL_SIZE*11, CELL_SIZE*11))
    B_GRID_POS = (SCREEN_WIDTH - (ROWS * CELL_SIZE) - CELL_SIZE, 0)
    SHIPS_ZONE = load_image('images/ships_zone.png',
                            (CELL_SIZE*11, CELL_SIZE*5))
    SHIPS_ZONE_POS = (0, CELL_SIZE*12)
    PLAYER_WIN = load_image('images/player_win.jpg',
                            (SCREEN_WIDTH, SCREEN_HEIGHT))
    DEFEAT = load_image('images/defeat.jpg', (SCREEN_WIDTH, SCREEN_HEIGHT))
