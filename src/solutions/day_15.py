from file_util import read_input_file
from run_util import RunTimer


def parse_input_file(add_disc: bool) -> list[tuple[int, int]]:
    lines = read_input_file(15)
    discs = []
    for i in range(len(lines)):
        parts = lines[i][:-1].split(" ")
        mod = int(parts[3])
        start = (int(parts[-1]) + i + 1) % mod
        discs.append((start, mod))
    if add_disc:
        discs.append(((len(lines) + 1) % 11, 11))
    return discs


def day_15(add_disc: bool) -> int:
    discs = parse_input_file(add_disc)
    for i in range(10000000):
        got_through = True
        for disc in discs:
            if (disc[0] + i) % disc[1] != 0:
                got_through = False
                break
        if got_through:
            return i
    raise RuntimeError("Couldn't find solution!")


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Times: {day_15(False)}, {day_15(True)}")
    timer.print()


def test_day_15():
    assert day_15(False) == 5
    assert day_15(True) == 85
