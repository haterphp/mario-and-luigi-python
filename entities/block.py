from pygame import draw, Rect

from common.coordinate import Coordinate
from scene import Scene
from .entity import Entity


class Block(Entity):
    def __init__(self, scene: Scene):
        BLOCK_COORDINATES = Coordinate(
            x=150,
            y=scene.screen.get_height() - 100,
            h=50,
            w=50
        )

        super().__init__(scene, BLOCK_COORDINATES)

        self._rect = Rect(
            self._coordinate.x,
            self._coordinate.y,
            self._coordinate.w,
            self._coordinate.h
        )

        self._color = (0, 0, 0)

    def draw(self):
        draw.rect(self._scene.screen, self._color, self._rect)

    def onCollisionStarted(self, entity: Entity):
        self._color = (0, 255, 0)

    def onCollisionEnded(self, entity: Entity):
        self._color = (0, 0, 0)
