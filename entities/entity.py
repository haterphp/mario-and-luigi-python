from typing import TypeVar, Tuple

from common.drawable import Drawable
from common.coordinate import Coordinate

from events import KeyEventSubscriber, CollisionEventSubscriber
from scene import Scene

TEntity = TypeVar("TEntity", bound="Entity")


class Entity(Drawable, KeyEventSubscriber, CollisionEventSubscriber):
    def __init__(self, scene: Scene, coordinate: Coordinate):
        self._coordinate = coordinate
        self._scene = scene

    def getCoordinate(self) -> Coordinate:
        return self._coordinate
