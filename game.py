import pygame

from typing import List

from common.drawable import Drawable
from entities import Player, Block
from events import KeyEventHandler, CollisionEventHandler
from scene import Scene


class Game:
    def __init__(self, screen: pygame.Surface):
        self.__scene = Scene(screen)
        self.__player = Player(self.__scene)
        self.__block = Block(self.__scene)

        self.__key_event = KeyEventHandler()
        self.__key_event.subscribe(self.__player)

        self.__collision_event = CollisionEventHandler()
        self.__collision_event.subscribe(self.__player)
        self.__collision_event.subscribe(self.__block)

        self.__drawable: List[Drawable] = [
            self.__scene,
            self.__block,
            self.__player,
        ]

    def draw(self):
        # Bind events observers
        self.__key_event.observe()
        self.__collision_event.observe()

        # Draw entities
        for entity in self.__drawable:
            entity.draw()

    def destroy(self):
        self.__key_event.unsubscribe(self.__player)
