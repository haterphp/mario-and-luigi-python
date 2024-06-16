from typing import List, TypeVar, Generic

Subscriber = TypeVar('Subscriber')


class EventHandler(Generic[Subscriber]):
    def __init__(self):
        self._subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def observe(self):
        pass