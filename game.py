import pygame

from typing import List

from common.drawable import Drawable
from entities import Player, Block
from events import KeyEventHandler
from map import Map
from scene import Scene


class Game:
    def __init__(self, scene: Scene):
        self.__player = Player(scene)
        self.__map = Map(scene)

        # Subscribe events
        self.__key_event = KeyEventHandler()
        self.__key_event.subscribe(self.__player)

        self.__player.subscribeEntitiesForCollision(self.__map.blocks)

        self.__drawable: List[Drawable] = [
            scene,
            self.__map,
            self.__player,
        ]

    def draw(self):
        # Observe events
        self.__key_event.observe()

        # Draw entities
        for entity in self.__drawable:
            entity.draw()

    def destroy(self):
        self.__key_event.unsubscribe(self.__player)
