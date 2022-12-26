from src.util.file_util import read_input_file


def day_02_1() -> str:
    keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    lines = read_input_file(2)
    x, y = 1, 1
    code = ""
    for line in lines:
        for char in line:
            if char == "U":
                y = max(y - 1, 0)
            elif char == "D":
                y = min(y + 1, 2)
            elif char == "L":
                x = max(x - 1, 0)
            elif char == "R":
                x = min(x + 1, 2)
            else:
                raise ValueError(f"Unknown command {char}")
        code += keypad[y][x]

    return code


def day_02_2() -> str:
    keypad = [
        ["", "", "1", "", ""],
        ["", "2", "3", "4", ""],
        ["5", "6", "7", "8", "9"],
        ["", "A", "B", "C", ""],
        ["", "", "D", "", ""],
    ]

    lines = read_input_file(2)
    x, y = 0, 2
    code = ""
    for line in lines:
        for char in line:
            if char == "U":
                new_x, new_y = x, max(y - 1, 0)
            elif char == "D":
                new_x, new_y = x, min(y + 1, 4)
            elif char == "L":
                new_x, new_y = max(x - 1, 0), y
            elif char == "R":
                new_x, new_y = min(x + 1, 4), y
            else:
                raise ValueError(f"Unknown command {char}")
            if keypad[new_y][new_x] != "":
                x, y = new_x, new_y
        code += keypad[y][x]

    return code


if __name__ == "__main__":
    print(f"Code (1): {day_02_1()}")
    print(f"Code (2): {day_02_2()}")
