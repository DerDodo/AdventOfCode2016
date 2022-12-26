from day_03 import is_triangle_possible


def test_day_03():
    assert is_triangle_possible(3, 3, 3) is True
    assert is_triangle_possible(5, 10, 25) is False
    assert is_triangle_possible(5, 10, 15) is False
    assert is_triangle_possible(6, 10, 15) is True
