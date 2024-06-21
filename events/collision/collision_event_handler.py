from typing import List

from common.collision import is_collision
from .collision_event_subscriber import CollisionEventSubscriber
from events.event_handler import EventHandler


class CollisionEventHandler(EventHandler[CollisionEventSubscriber]):
    def __init__(self, target: CollisionEventSubscriber):
        super().__init__()
        self._target = target
        self._intersected_subscribers: List[CollisionEventSubscriber] = []

    def observe(self):
        for subscriber in self._subscribers:

            targetPosition = self._target.getCoordinate()
            subscriberPosition = subscriber.getCoordinate()

            if is_collision(targetPosition, subscriberPosition):
                self._target.onCollision(subscriber)
                subscriber.onCollision(self._target)

                if subscriber not in self._intersected_subscribers:
                    self._intersected_subscribers.append(subscriber)

                    self._target.onCollisionStarted(subscriber)
                    subscriber.onCollisionStarted(self._target)

            elif subscriber in self._intersected_subscribers:
                self._intersected_subscribers.remove(subscriber)

                self._target.onCollisionEnded(subscriber)
                subscriber.onCollisionEnded(self._target)
