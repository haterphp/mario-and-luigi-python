from pygame import Rect

from .entity import Entity


class SceneEntity(Entity):
    def _defineDrawableEntity(self) -> Rect:
        return Rect(
            self._coordinate.x - self._scene.offset,
            self._coordinate.y,
            self._coordinate.w,
            self._coordinate.h,
        )