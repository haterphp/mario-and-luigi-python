from pygame import Rect, draw, K_LEFT, K_RIGHT

from typing import Optional, Tuple

from scene import Scene
from .entity import Entity
from variables import PLAYER_COORDINATE, PLAYER_SPEED, PLAYER_SPEED_VERTICAL, GRAVITY, SCENE_SIZE


class Player(Entity):
    def __init__(self, scene: Scene):
        PLAYER_COORDINATE.y = scene.screen.get_height() - PLAYER_COORDINATE.h
        super().__init__(PLAYER_COORDINATE)
        self.__scene = scene

        # Visual player attributes
        self.__rect: Optional[Rect] = None
        self.__syncRect()

        # Jump attributes
        self.__jumpCount = 0

    def draw(self):
        if self.__rect is not None:
            draw.rect(self.__scene.screen, (255, 0, 0), self.__rect)

    def onKeyPress(self, key: Tuple[bool]):
        HALF_SCENE = self.__scene.screen.get_width() / 2 + PLAYER_SPEED

        if key[K_LEFT]:
            speed = -PLAYER_SPEED
            if self.__scene.offset > 0 and self._coordinate.right < HALF_SCENE:
                self.__scene.move(speed)
            elif self._coordinate.left > 0:
                self._coordinate.moveX(speed)

        elif key[K_RIGHT]:
            speed = PLAYER_SPEED
            if self.__scene.offset < SCENE_SIZE and self._coordinate.right >= HALF_SCENE:
                self.__scene.move(speed)
            elif self._coordinate.right < self.__scene.screen.get_width():
                self._coordinate.moveX(speed)

        self.__syncRect()

    def __jump(self):
        self.__jumpCount += 1
        self._coordinate.moveY(PLAYER_SPEED_VERTICAL - GRAVITY * self.__jumpCount)


    def __syncRect(self):
        self.__rect = Rect(
            self._coordinate.x,
            self._coordinate.y,
            self._coordinate.w,
            self._coordinate.h
        )

