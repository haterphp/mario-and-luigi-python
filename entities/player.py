from pygame import K_LEFT, K_RIGHT

from typing import Tuple, List

from events import CollisionEventHandler, CollisionEventSubscriber
from scene import Scene
from .entity import Entity
from variables import PLAYER_COORDINATE, PLAYER_SPEED, PLAYER_SPEED_VERTICAL, GRAVITY, SCENE_SIZE


class Player(Entity):
    def __init__(self, scene: Scene):
        PLAYER_COORDINATE.y = scene.screen.get_height() - PLAYER_COORDINATE.h
        super().__init__(scene,  PLAYER_COORDINATE)

        self._color = (255, 0, 0)

        # Collision
        self.__collision_event = CollisionEventHandler(self)

        # Jump attributes
        self.__jumpCount = 0

    def draw(self):
        super().draw()
        self.__collision_event.observe()

    def onKeyPress(self, key: Tuple[bool]):
        HALF_SCENE = self._scene.screen.get_width() / 2 + PLAYER_SPEED

        if key[K_LEFT]:
            speed = -PLAYER_SPEED
            if self._scene.offset > 0 and self._coordinate.right < HALF_SCENE:
                self._scene.move(speed)
            elif self._coordinate.left > 0:
                self._coordinate.moveX(speed)

        elif key[K_RIGHT]:
            speed = PLAYER_SPEED
            if self._scene.offset < SCENE_SIZE and self._coordinate.right >= HALF_SCENE:
                self._scene.move(speed)
            elif self._coordinate.right < self._scene.screen.get_width():
                self._coordinate.moveX(speed)

    def subscribeEntitiesForCollision(self, subscribers: List[CollisionEventSubscriber]):
        for subscriber in subscribers:
            self.__collision_event.subscribe(subscriber)

    def __jump(self):
        self.__jumpCount += 1
        self._coordinate.moveY(PLAYER_SPEED_VERTICAL - GRAVITY * self.__jumpCount)

