from common.drawable import Drawable
from scene import Scene


class Map(Drawable):
    def __init__(self, scene: Scene):
        self.__scene = scene

