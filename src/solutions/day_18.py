from file_util import read_input_file
from run_util import RunTimer


def parse_input_file() -> list[bool]:
    line = read_input_file(18)[0]
    return [c == "^" for c in line]


def calc_next_row(source: list[bool], target: list[bool]):
    for i in range(1, len(source) - 1):
        target[i] = source[i - 1] != source[i + 1]


def day_18(distance: int) -> int:
    row1 = parse_input_file()
    row1.insert(0, False)
    row1.append(False)
    num_safe_tiles = row1.count(False) - 2

    row2 = [False] * len(row1)

    for i in range(distance - 1):
        if i % 2 == 0:
            calc_next_row(row1, row2)
            num_safe_tiles += row2.count(False) - 2
        else:
            calc_next_row(row2, row1)
            num_safe_tiles += row1.count(False) - 2

    return num_safe_tiles


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Safe tiles: {day_18(40), day_18(400000)}")
    timer.print()


def test_day_18():
    assert day_18(10) == 38
