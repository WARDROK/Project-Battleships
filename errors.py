class LowWidthResolution(Exception):
    def __init__(self, width) -> None:
        super().__init__(
            f'Width resolution must be minimum 800. Actual: {width}')
        self.width = width


class LowHeightResolution(Exception):
    def __init__(self, height) -> None:
        super().__init__(
            f'Height resolution must be minimum 600. Actual: {height}')
        self.height = height


class WrongResolutionData(Exception):
    def __init__(self) -> None:
        super().__init__("\nWrong data in screen_resolution.txt\n\
Example correct format:\n\
screen_width=1280\n\
screen_height=720")


class NotFile(Exception):
    def __init__(self) -> None:
        super().__init__("Cannot find screen_resolution.txt\n\
screen_resolution.txt was created with default settings\n\
You can restart with default settings or set own")
