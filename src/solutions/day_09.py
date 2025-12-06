from file_util import read_input_file
from run_util import RunTimer


def read_input() -> str:
    return read_input_file(9)[0]


def read_marker(compressed: str, i: int) -> tuple[int, int, int]:
    length = 0
    times = 0
    read_length = True
    i += 1
    while compressed[i] != ")":
        if compressed[i] == "x":
            read_length = False
        elif read_length:
            length = length * 10 + int(compressed[i])
        else:
            times = times * 10 + int(compressed[i])
        i += 1
    i += 1
    return i, length, times


def decompress(compressed: str) -> tuple[int, int]:
    decompressed_length_v1 = 0
    decompressed_length_v2 = 0
    i = 0
    while i < len(compressed):
        if compressed[i] == "(":
            i, length, times = read_marker(compressed, i)
            decompressed_length_v1 += length * times
            decompressed_length_v2 += decompress(compressed[i:i + length])[1] * times
            i += length
        else:
            decompressed_length_v1 += 1
            decompressed_length_v2 += 1
            i += 1
    return decompressed_length_v1, decompressed_length_v2


def day_09() -> tuple[int, int]:
    compressed = read_input()
    return decompress(compressed)


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Decompressed length: {day_09()}")
    timer.print()


def test_day_09():
    assert day_09() == (29, 49)
