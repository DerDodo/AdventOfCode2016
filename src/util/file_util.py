import sys
from typing import List


def read_input_file(level_id: int, strip: bool = True) -> List[str]:
    file_id = f"{level_id:02d}"
    if "pytest" in sys.modules:
        file_id += "t"

    return read_input_file_id(file_id, strip)


def read_input_file_id(file_id: str, strip: bool = True) -> List[str]:
    input_file = open(f"../../input-files/day-{file_id}.txt", "r")
    lines = input_file.readlines()
    if strip:
        lines = [line.strip() for line in lines]
    return lines
