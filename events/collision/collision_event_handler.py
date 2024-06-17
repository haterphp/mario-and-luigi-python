from .collision_event_subscriber import CollisionEventSubscriber
from events.event_handler import EventHandler


class CollisionEventHandler(EventHandler[CollisionEventSubscriber]):
    def observe(self):
        for currentSubscriber in self._subscribers:
            for subscriber in self._subscribers:

                if currentSubscriber is subscriber:
                    continue

                currentSubscriberPosition = currentSubscriber.getCoordinate()
                otherSubscriberPosition = subscriber.getCoordinate()

                if (currentSubscriberPosition.left < otherSubscriberPosition.right and
                        otherSubscriberPosition.left < currentSubscriberPosition.right and
                        currentSubscriberPosition.top < otherSubscriberPosition.bottom and
                        otherSubscriberPosition.top < currentSubscriberPosition.bottom):

                    currentSubscriber.onCollisionStarted(subscriber)
                    subscriber.onCollisionStarted(currentSubscriber)

