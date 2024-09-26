CSI = lambda n: f"\033[{n}m"

class Color:
    BLACK = CSI(30)
    RED = CSI(31)
    GREEN = CSI(32)
    YELLOW = CSI(33)
    BLUE = CSI(34)
    MAGENTA = CSI(35)
    CYAN = CSI(36)
    WHITE = CSI(37)
    RESET = CSI(39)

HEADER = f"""{Color.BLUE}
.______    _______ .__   __. .__   __. ____    ____  _______.  ______      __    __   __   ________
|   _  \  |   ____||  \ |  | |  \ |  | \   \  /   / /       | /  __  \    |  |  |  | |  | |       /
|  |_)  | |  |__   |   \|  | |   \|  |  \   \/   / |   (----`|  |  |  |   |  |  |  | |  | `---/  /
|   _  <  |   __|  |  . `  | |  . `  |   \_    _/   \   \    |  |  |  |   |  |  |  | |  |    /  /
|  |_)  | |  |____ |  |\   | |  |\   |     |  | .----)   |   |  `--'  '--.|  `--'  | |  |   /  /----.
|______/  |_______||__| \__| |__| \__|     |__| |_______/     \_____\_____\\______/  |__|  /________|
"""

class Header:
    title: str

    def __init__(self, title: str) -> None:
        self.title = title

    def __str__(self):
        return "\n".join(
            [
                HEADER,
                " " * int((73 - len(self.title)) / 2) + self.title + "\n",
                "-" * 73,
            ]
        )
