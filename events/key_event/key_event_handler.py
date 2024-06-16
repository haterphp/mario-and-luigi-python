from pygame.key import get_pressed

from .key_event_subscriber import KeyEventSubscriber
from ..event_handler import EventHandler


class KeyEventHandler(EventHandler[KeyEventSubscriber]):

    def observe(self):
        for subscriber in self._subscribers:
            keys = get_pressed()
            subscriber.onKeyPress(keys)
