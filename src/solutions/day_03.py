from typing import List

from run_util import RunTimer
from src.util.file_util import read_input_file


def is_triangle_possible(a, b, c) -> bool:
    return a + b > c and a + c > b and b + c > a


def line_to_list(line: str) -> List[int]:
    return list(map(int, filter(lambda p: p != "", line.split(" "))))


def lines_to_triangles(lines: List[str]) -> List[List[int]]:
    return list(map(line_to_list, lines))


def columns_to_triangles(lines: List[str]) -> List[List[int]]:
    triangles = []
    for i in range(0, len(lines), 3):
        line_1 = line_to_list(lines[i])
        line_2 = line_to_list(lines[i + 1])
        line_3 = line_to_list(lines[i + 2])
        for j in range(3):
            triangles.append([line_1[j], line_2[j], line_3[j]])
    return triangles


def day_03_1() -> int:
    lines = read_input_file(3)
    return len(list(filter(lambda t: is_triangle_possible(t[0], t[1], t[2]), lines_to_triangles(lines))))


def day_03_2() -> int:
    lines = read_input_file(3)
    return len(list(filter(lambda t: is_triangle_possible(t[0], t[1], t[2]), columns_to_triangles(lines))))


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Possible triangles (1): {day_03_1()}")
    print(f"Possible triangles (2): {day_03_2()}")
    timer.print()


def test_day_03():
    assert is_triangle_possible(3, 3, 3) is True
    assert is_triangle_possible(5, 10, 25) is False
    assert is_triangle_possible(5, 10, 15) is False
    assert is_triangle_possible(6, 10, 15) is True
