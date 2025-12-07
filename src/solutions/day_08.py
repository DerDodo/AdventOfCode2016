from enum import Enum

from file_util import read_input_file
from math_util import Area, Position
from run_util import RunTimer


def command_rect(screen: Area, width: int, height: int):
    for x in range(width):
        for y in range(height):
            screen.set(x, y, "#")


def command_shift_row(screen: Area, y: int, by: int):
    width = screen.get_width()
    temp = [False for _ in range(width)]
    for x in range(width):
        temp[x] = screen.field[y][x]
    for x in range(width):
        screen.field[y][(x + by) % width] = temp[x]


def command_shift_column(screen: Area, x: int, by: int):
    height = screen.get_height()
    temp = [False for _ in range(height)]
    for y in range(height):
        temp[y] = screen.field[y][x]
    for y in range(height):
        screen.field[(y + by) % height][x] = temp[y]


class Command(Enum):
    Rect = "rect"
    ShiftRow = "row"
    ShiftColumn = "column"

    def execute(self, screen: Area, param1: int, param2: int):
        if self == Command.Rect:
            command_rect(screen, param1, param2)
        elif self == Command.ShiftRow:
            command_shift_row(screen, param1, param2)
        elif self == Command.ShiftColumn:
            command_shift_column(screen, param1, param2)


def read_input() -> list[tuple[Command, int, int]]:
    lines = read_input_file(8)
    commands = []
    for line in lines:
        parts = line.split(" ")
        if parts[0] == Command.Rect.value:
            dimensions = parts[1].split("x")
            commands.append((Command.Rect, int(dimensions[0]), int(dimensions[1])))
        elif parts[1] == Command.ShiftRow.value:
            commands.append((Command.ShiftRow, int(parts[2][2:]), int(parts[-1])))
        elif parts[1] == Command.ShiftColumn.value:
            commands.append((Command.ShiftColumn, int(parts[2][2:]), int(parts[-1])))
    return commands


def read_font() -> dict[str, list[str]]:
    input_file = open("day_08_font.txt", "r")
    lines = input_file.readlines()
    font = {}
    for col in range(0, len(lines[-1]), 5):
        font[lines[0][col]] = [lines[i][col:col+5] for i in range(1, len(lines))]
    return font


def match_letter(screen: Area, start: int, font: dict[str, list[str]]) -> str:
    for letter in font.items():
        matched = True
        for line_i in range(len(letter[1])):
            for col in range(5):
                if letter[1][line_i][col] != screen.field[line_i][start+col]:
                    matched = False
                    break
        if matched:
            return letter[0]
    raise ValueError("Couldn't match letter!")


def day_08(width: int, height: int, check_text: bool) -> tuple[int, str]:
    screen = Area.from_bounds_and_value(Position(width, height), ".")
    commands = read_input()
    for command in commands:
        command[0].execute(screen, command[1], command[2])
    text = ""
    if check_text:
        font = read_font()
        for col in range(0, screen.get_width(), 5):
            text += match_letter(screen, col, font)
    return screen.count("#"), text


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Num active pixels: {day_08(50, 6, True)}")
    timer.print()


def test_day_08():
    assert day_08(7, 3, False) == (9, "")
