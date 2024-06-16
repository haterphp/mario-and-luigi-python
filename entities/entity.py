from typing import TypeVar, Tuple

from common.drawable import Drawable
from common.coordinate import Coordinate

from events import KeyEventSubscriber

TEntity = TypeVar("TEntity", bound="Entity")


class Entity(Drawable, KeyEventSubscriber):
    def __init__(self, coordinate: Coordinate):
        self._coordinate = coordinate

    def onCollision(self, entity: TEntity):
        pass
