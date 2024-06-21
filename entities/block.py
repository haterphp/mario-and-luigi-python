from common.coordinate import Coordinate
from scene import Scene

from .scene_entity import SceneEntity


class Block(SceneEntity):
    def __init__(self, scene: Scene, coordinate: Coordinate):
        super().__init__(scene, coordinate)

    def onCollisionStarted(self, entity: SceneEntity):
        self._color = (0, 255, 0)

    def onCollisionEnded(self, entity: SceneEntity):
        self._color = (0, 0, 0)
