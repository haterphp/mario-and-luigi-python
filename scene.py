from pygame import Surface

from common.drawable import Drawable
from variables import SCREEN_BACKGROUND


class Scene(Drawable):
    def __init__(self, screen: Surface):

        self.offset = 0
        self.screen = screen

    def move(self, offset: int):
        self.offset += offset

    def draw(self):
        self.screen.fill(SCREEN_BACKGROUND)
        # print('screen offset', self.offset)

