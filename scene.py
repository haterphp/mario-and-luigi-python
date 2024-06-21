from pygame.display import set_mode

from common.drawable import Drawable
from variables import SCREEN_BACKGROUND, SCREEN_WIDTH, SCREEN_HEIGHT


class Scene(Drawable):
    def __init__(self):
        self.offset = 0
        self.screen = set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def move(self, offset: int):
        self.offset += offset

    def draw(self):
        self.screen.fill(SCREEN_BACKGROUND)


