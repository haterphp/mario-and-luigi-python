from typing import TypeVar, Tuple, Optional

from pygame import Rect, draw

from common.drawable import Drawable
from common.coordinate import Coordinate

from events import KeyEventSubscriber, CollisionEventSubscriber
from scene import Scene

TEntity = TypeVar("TEntity", bound="Entity")


class Entity(Drawable, KeyEventSubscriber, CollisionEventSubscriber):
    def __init__(self, scene: Scene, coordinate: Coordinate):
        self._coordinate = coordinate
        self._scene = scene

        self._color = (0, 0, 0)

    def draw(self):
        rect = self._defineDrawableEntity()
        draw.rect(self._scene.screen, self._color, rect)

    def getCoordinate(self) -> Coordinate:
        return self._coordinate

    def _defineDrawableEntity(self) -> Rect:
        return Rect(
            self._coordinate.x,
            self._coordinate.y,
            self._coordinate.w,
            self._coordinate.h
        )

