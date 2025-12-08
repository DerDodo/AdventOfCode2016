import hashlib

from math_util import Position, Direction
from run_util import RunTimer

direction_code = {
    Direction.North: "U",
    Direction.South: "D",
    Direction.West: "L",
    Direction.East: "R",
}


def is_open_door(hex_code: str) -> bool:
    return hex_code == "b" or hex_code == "c" or hex_code == "d" or hex_code == "e" or hex_code == "f"


def calc_next_moves(passcode: str, path: str, position: Position) -> set[Direction]:
    hash_value = hashlib.md5((passcode + path).encode()).hexdigest()
    directions = set()
    if is_open_door(hash_value[0]) and position.y != 0:
        directions.add(Direction.North)
    if is_open_door(hash_value[1]) and position.y != 3:
        directions.add(Direction.South)
    if is_open_door(hash_value[2]) and position.x != 0:
        directions.add(Direction.West)
    if is_open_door(hash_value[3]) and position.x != 3:
        directions.add(Direction.East)
    return directions


def day_17(passcode: str) -> tuple[str | None, int]:
    paths: set[tuple[str, Position]] = {("", Position(0, 0))}
    shortest_path = None
    longest_path = 0
    while len(paths) > 0:
        new_paths: set[tuple[str, Position]] = set()
        for path in paths:
            directions = calc_next_moves(passcode, path[0], path[1])
            for direction in directions:
                new_path = path[0] + direction_code[direction]
                new_position = path[1] + direction
                if new_position.x == 3 and new_position.y == 3:
                    longest_path = len(new_path)
                    if shortest_path is None:
                        shortest_path = new_path
                else:
                    new_paths.add((new_path, new_position))
        paths = new_paths
    return shortest_path, longest_path


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Paths: {day_17('qzthpkfp')}")
    timer.print()


def test_day_17():
    assert day_17("hijkl") == (None, 0)
    assert day_17("ihgpwlah") == ("DDRRRD", 370)
    assert day_17("kglvqrro") == ("DDUDRLRRUDRD", 492)
    assert day_17("ulqzkmiv") == ("DRURDRUDDLLDLUURRDULRLDUUDDDRR", 830)