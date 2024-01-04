class LowWidthResolution(Exception):
    def __init__(self, width) -> None:
        super().__init__(
            f"\nWidth resolution must be minimum 800. Entered: {width}\n\
'screen_resolution.txt' was set to default\n\
Please run game again with deafult resolution\n\
or set your own with correct data")
        self.width = width


class LowHeightResolution(Exception):
    def __init__(self, height) -> None:
        super().__init__(
            f"\nHeight resolution must be minimum 600. Entered: {height}\n\
'screen_resolution.txt' was set to default\n\
Please run game again with deafult resolution\n\
or set your own with correct data")
        self.height = height


class WrongResolutionData(Exception):
    def __init__(self) -> None:
        super().__init__("\nWrong data in 'screen_resolution.txt'\n\n\
Example correct format:\n\
screen_width=1280\n\
screen_height=720\n\n\
'screen_resolution.txt' was set to default\n\
Please run game again with deafult resolution\n\
or set your own with correct data")


class NotFile(Exception):
    def __init__(self) -> None:
        super().__init__("\nCannot find file: 'screen_resolution.txt'\n\
'screen_resolution.txt' was created with default settings\n\
You can restart with default settings or set your own")
