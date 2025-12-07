from enum import Enum
from math import prod

from file_util import read_input_file
from run_util import RunTimer


class PassTo(Enum):
    Output = "output"
    Bot = "bot"


class Chip(Enum):
    High = "high"
    Low = "low"


class Bot:
    id: int
    chips: set[int]
    rules: dict[Chip, tuple[PassTo, int]]

    def __init__(self, id: int):
        self.id = id
        self.chips = set()
        self.rules = {}

    def add(self, chip: int):
        self.chips.add(chip)

    def remove(self, chip: Chip) -> tuple[int, PassTo, int]:
        if chip == Chip.High:
            value = max(self.chips)
        else:
            value = min(self.chips)
        self.chips.remove(value)
        return value, self.rules[chip][0], self.rules[chip][1]

    def pass_chip(self, chip: Chip, bots: dict, outputs: dict[int, int]):
        value, pass_to, target = self.remove(chip)
        if pass_to == PassTo.Bot:
            bots[target].add(value)
        else:
            outputs[target] = value

    def pass_chips(self, bots: dict, outputs: dict[int, int]):
        self.pass_chip(Chip.High, bots, outputs)
        self.pass_chip(Chip.Low, bots, outputs)

    def __getitem__(self, item: Chip) -> int:
        if item == Chip.High:
            return max(self.chips)
        else:
            return min(self.chips)

    def __str__(self) -> str:
        return f"Bot {self.id} has {' and '.join(map(str, self.chips))}"


def read_input() -> dict[int, Bot]:
    lines = read_input_file(10)
    bots: dict[int, Bot] = {}
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "value":
            bot_id = int(parts[-1])
            if bot_id not in bots:
                bots[bot_id] = Bot(bot_id)
            bots[bot_id].add(int(parts[1]))
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "bot":
            bot_id = int(parts[1])
            if bot_id not in bots:
                bots[bot_id] = Bot(bot_id)
            bots[bot_id].rules[Chip(parts[3])] = (PassTo(parts[5]), int(parts[6]))
            bots[bot_id].rules[Chip(parts[-4])] = (PassTo(parts[-2]), int(parts[-1]))
    return bots


def get_acting_bots(bots: dict[int, Bot]) -> set[int]:
    acting_bots = set()
    for bot in bots.values():
        if len(bot.chips) == 2:
            acting_bots.add(bot.id)
    return acting_bots


def day_10(chip1: int, chip2: int, interest_outputs: list[int]) -> tuple[int, int]:
    low_interest = min(chip1, chip2)
    high_interest = max(chip1, chip2)
    bot_interest = -1
    bots = read_input()
    outputs = {}
    for _ in range(100000):
        acting_bots = get_acting_bots(bots)
        if len(acting_bots) == 0:
            break

        for acting_bot_id in acting_bots:
            acting_bot = bots[acting_bot_id]

            if acting_bot[Chip.Low] == low_interest and acting_bot[Chip.High] == high_interest and bot_interest == -1:
                bot_interest = acting_bot.id

            acting_bot.pass_chips(bots, outputs)

    output_value = prod([outputs[interest_output] for interest_output in interest_outputs])
    return bot_interest, output_value


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Target bot: {day_10(61, 17, [0, 1, 2])}")
    timer.print()


def test_day_10():
    assert day_10(2, 5, [0, 1]) == (2, 10)
