from typing import List

from common.coordinate import Coordinate
from common.drawable import Drawable
from entities import Block
from scene import Scene
from variables import SCREEN_HEIGHT

COORDINATE = Coordinate(50, SCREEN_HEIGHT - 100, 50, 50)

class Map(Drawable):
    def __init__(self, scene: Scene):
        self.__scene = scene

        self.__blocks: List[Block] = [
            Block(scene, COORDINATE)
        ]

    @property
    def blocks(self) -> List[Block]:
        return self.__blocks

    def draw(self):
        for block in self.__blocks:
            block.draw()

