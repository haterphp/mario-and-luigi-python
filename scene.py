from pygame import Surface

from common.coordinate import Coordinate
from common.drawable import Drawable
from map import Map
from variables import SCREEN_BACKGROUND

BLOCK_COORDINATES = [
    Coordinate(
        x=150,
        y=0,
        h=50,
        w=50
    ),
    Coordinate(
        x=250,
        y=0,
        h=50,
        w=50
    ),
]

class Scene(Drawable):
    def __init__(self, screen: Surface):
        self.offset = 0
        self.screen = screen

        self.__map = Map(self)

    def move(self, offset: int):
        self.offset += offset

    def draw(self):
        self.screen.fill(SCREEN_BACKGROUND)
        self.__map.draw()


