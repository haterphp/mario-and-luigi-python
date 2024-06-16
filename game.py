import pygame

from typing import List

from common.drawable import Drawable
from entities import Player
from events import KeyEventHandler
from scene import Scene


class Game:
    def __init__(self, screen: pygame.Surface):
        self.__scene = Scene(screen)
        self.__player = Player(self.__scene)

        self.__key_event = KeyEventHandler()
        self.__key_event.subscribe(self.__player)

        self.__drawable: List[Drawable] = [self.__scene, self.__player]

    def draw(self):
        # Bind events observers
        self.__key_event.observe()

        # Draw entities
        for entity in self.__drawable:
            entity.draw()

    def destroy(self):
        self.__key_event.unsubscribe(self.__player)
