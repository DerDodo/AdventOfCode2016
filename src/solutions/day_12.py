from abc import abstractmethod, ABC

from file_util import read_input_file
from run_util import RunTimer


class Operation(ABC):
    @abstractmethod
    def exec(self, instruction_counter: int, registers: dict[str, int]) -> int:
        pass


class Inc(Operation):
    register: str

    def __init__(self, register: str):
        self.register = register

    def exec(self, instruction_counter: int, registers: dict[str, int]) -> int:
        registers[self.register] = registers[self.register] + 1
        return instruction_counter + 1


class Dec(Operation):
    register: str

    def __init__(self, register: str):
        self.register = register

    def exec(self, instruction_counter: int, registers: dict[str, int]) -> int:
        registers[self.register] = registers[self.register] - 1
        return instruction_counter + 1


class Cpy(Operation):
    value: str
    register: str

    def __init__(self, value: str, register: str):
        self.value = value
        self.register = register

    def exec(self, instruction_counter: int, registers: dict[str, int]) -> int:
        if self.value.isnumeric():
            registers[self.register] = int(self.value)
        else:
            registers[self.register] = registers[self.value]
        return instruction_counter + 1


class Jnz(Operation):
    value: str
    jump_by: int

    def __init__(self, value: str, jump_by: int):
        self.value = value
        self.jump_by = jump_by

    def exec(self, instruction_counter: int, registers: dict[str, int]) -> int:
        if self.value.isnumeric():
            value = int(self.value)
        else:
            value = registers[self.value]

        if value != 0:
            return instruction_counter + self.jump_by
        else:
            return instruction_counter + 1


def create_operation(command: str) -> Operation:
    parts = command.split(" ")
    if parts[0] == "inc":
        return Inc(parts[1])
    elif parts[0] == "dec":
        return Dec(parts[1])
    elif parts[0] == "cpy":
        return Cpy(parts[1], parts[2])
    else:
        return Jnz(parts[1], int(parts[2]))


class Computer:
    registers: dict[str, int]
    operations: list[Operation]

    def __init__(self, source_code: list[str], c_value: int):
        self.registers = {
            "a": 0,
            "b": 0,
            "c": c_value,
            "d": 0,
        }
        self.operations = [create_operation(line) for line in source_code]

    def run(self) -> int:
        instruction_counter = 0
        while instruction_counter < len(self.operations):
            instruction_counter = self.operations[instruction_counter].exec(instruction_counter, self.registers)
        return self.registers["a"]


def read_input(c_value: int) -> Computer:
    return Computer(read_input_file(12), c_value)


def day_12(c_value: int) -> int:
    computer = read_input(c_value)
    return computer.run()


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Num steps: {day_12(0)}, {day_12(1)}")
    timer.print()


def test_day_12():
    assert day_12(0) == 42
    assert day_12(1) == 42
