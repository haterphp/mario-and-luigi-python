from typing import TypeVar

from common.coordinate import Coordinate

TCollisionEventSubscriber = TypeVar("TCollisionEventSubscriber", bound="CollisionEventSubscriber")


class CollisionEventSubscriber:
    def getCoordinate(self) -> Coordinate:
        pass

    def onCollisionStarted(self, entity: TCollisionEventSubscriber):
        pass

    def onCollisionEnded(self, entity: TCollisionEventSubscriber):
        pass
