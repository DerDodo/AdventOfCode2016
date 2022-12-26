from src.solutions.day_01 import day_01_1, day_01_2


def test_day_01():
    assert day_01_1("R2, L3") == 5
    assert day_01_1("R2, R2, R2") == 2
    assert day_01_1("R5, L5, R5, R3") == 12
    assert day_01_2("R8, R4, R4, R8") == 4
