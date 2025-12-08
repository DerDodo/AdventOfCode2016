from run_util import RunTimer


def extend(data: list[int]):
    data.append(0)
    for i in range(len(data) - 2, -1, -1):
        data.append(1 - data[i])


def calc_checksum(data: list[int]) -> str:
    checksum = data.copy()
    while len(checksum) % 2 == 0:
        next_checksum = []
        for i in range(0, len(checksum), 2):
            next_checksum.append(1 if checksum[i] == checksum[i + 1] else 0)
        checksum = next_checksum
    return "".join(list(map(str, checksum)))


def day_16(data_str: str, file_size: int) -> str:
    data = [1 if d == "1" else 0 for d in data_str]
    while len(data) < file_size:
        extend(data)
    return calc_checksum(data[:file_size])


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Checksum: {day_16('11101000110010100', 272), day_16('11101000110010100', 35651584)}")
    timer.print()


def test_day_16():
    assert day_16("10000", 20) == "01100"
