from file_util import read_input_file


def read_input() -> list[list[str]]:
    lines = read_input_file(6)
    columns = []
    for column in range(len(lines[0])):
        new_column = []
        for line in lines:
            new_column.append(line[column])
        columns.append(new_column)
    return columns


def day_06() -> tuple[str, str]:
    columns = read_input()
    solution_most_common = ""
    solution_least_common = ""
    for column in columns:
        column_set = set(column)
        solution_most_common += max(column_set, key=column.count)
        solution_least_common += min(column_set, key=column.count)
    return solution_most_common, solution_least_common


if __name__ == "__main__":
    print(f"Password (1): {day_06()}")


def test_day_06():
    assert day_06() == ("easter", "advent")
