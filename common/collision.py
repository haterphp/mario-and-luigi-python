from common.coordinate import Coordinate


def is_collision(c1: Coordinate, c2: Coordinate) -> bool:
    return (c1.left < c2.right and
            c2.left < c1.right and
            c1.top < c2.bottom and
            c2.top < c1.bottom)
