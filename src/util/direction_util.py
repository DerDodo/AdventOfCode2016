from enum import Enum
from typing import Tuple


class Coordinate:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) == int:
            return Coordinate(self.x + other, self.y + other)
        elif type(other) == Coordinate:
            return Coordinate(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented(f"Cannot add {type(other)} to Coordinate")

    def __sub__(self, other):
        if type(other) == int:
            return Coordinate(self.x - other, self.y - other)
        elif type(other) == Coordinate:
            return Coordinate(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented(f"Cannot subtract {type(other)} from Coordinate")

    def __mul__(self, other):
        if type(other) == int:
            return Coordinate(self.x * other, self.y * other)
        elif type(other) == Coordinate:
            return Coordinate(self.x * other.x, self.y * other.y)
        else:
            return NotImplemented(f"Cannot multiply {type(other)} from Coordinate")

    def manhattan_length(self) -> int:
        return abs(self.x) + abs(self.y)

    def to_tuple(self) -> Tuple[int, int]:
        return self.x, self.y


class Direction(Enum):
    North = Coordinate(0, -1)
    East = Coordinate(1, 0)
    South = Coordinate(0, 1)
    West = Coordinate(-1, 0)

    def turn_right(self):
        if self == Direction.North:
            return Direction.East
        elif self == Direction.East:
            return Direction.South
        elif self == Direction.South:
            return Direction.West
        else:
            return Direction.North

    def turn_left(self):
        if self == Direction.North:
            return Direction.West
        elif self == Direction.West:
            return Direction.South
        elif self == Direction.South:
            return Direction.East
        else:
            return Direction.North
