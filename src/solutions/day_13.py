from enum import Enum

from data_util import create_2d_list
from math_util import Position, Area, NEWSDirections
from run_util import RunTimer


class Field(Enum):
    Free = "."
    Cubicle = "#"


def is_cubicle(c: Position, favorite_number: int) -> bool:
    value = c.x * c.x + 3 * c.x + 2 * c.x * c.y + c.y + c.y * c.y + favorite_number
    div = 1
    num_ones = 0
    while div <= value:
        num_ones += 1 if value & div else 0
        div *= 2
    return num_ones % 2 == 1


def find_path(office: Area, target: Position) -> int:
    open_positions: set[Position] = {Position(1, 1)}
    visited = set(open_positions)
    for steps in range(10000):
        new_positions = set()
        for open_position in open_positions:
            for direction in NEWSDirections:
                new_position = open_position + direction
                if new_position == target:
                    return steps + 1
                if office.is_in_bounds(new_position) and office[new_position] == Field.Free and new_position not in visited:
                    new_positions.add(new_position)
                    visited.add(new_position)
        open_positions = new_positions
    raise RuntimeError("Couldn't find path!")


def fill(office: Area, steps: int) -> int:
    open_positions: set[Position] = {Position(1, 1)}
    visited = set(open_positions)
    for _ in range(steps):
        new_positions = set()
        for open_position in open_positions:
            for direction in NEWSDirections:
                new_position = open_position + direction
                if office.is_in_bounds(new_position) and office[new_position] == Field.Free and new_position not in visited:
                    new_positions.add(new_position)
                    visited.add(new_position)
        open_positions = new_positions
    return len(visited)


def day_13(favorite_number: int, target: Position) -> tuple[int, int]:
    office = Area(create_2d_list(target.x * 2, target.y * 2, Field.Free))
    for field in office:
        if is_cubicle(field, favorite_number):
            office[field] = Field.Cubicle
    return find_path(office, target), fill(office, 50)


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Num steps, positions: {day_13(1358, Position(31,39))}")
    timer.print()


def test_day_13():
    assert day_13(10, Position(7,4)) == (11, 20)
