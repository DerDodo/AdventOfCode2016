from src.util.direction_util import Coordinate, Direction
from src.util.file_util import read_input_file


def day_01_1(text: str) -> int:
    position = Coordinate(0, 0)
    direction = Direction.North
    commands = text.split(", ")
    for command in commands:
        if command[0] == "R":
            direction = direction.turn_right()
        elif command[0] == "L":
            direction = direction.turn_left()
        else:
            raise ValueError(f"Cannot parse {command}")

        position += direction.value * int(command[1:])
    return position.manhattan_length()


def day_01_2(text: str) -> int:
    position = Coordinate(0, 0)
    direction = Direction.North
    position_cache = set(position.to_tuple())

    commands = text.split(", ")
    for command in commands:
        if command[0] == "R":
            direction = direction.turn_right()
        elif command[0] == "L":
            direction = direction.turn_left()
        else:
            raise ValueError(f"Cannot parse {command}")

        for _ in range(int(command[1:])):
            position += direction.value
            if position.to_tuple() in position_cache:
                return position.manhattan_length()
            position_cache.add(position.to_tuple())

    raise ValueError("Didn't visit anything twice!")


if __name__ == "__main__":
    print(f"Distance (1): {day_01_1(read_input_file(1)[0])}")
    print(f"Distance (2): {day_01_2(read_input_file(1)[0])}")
