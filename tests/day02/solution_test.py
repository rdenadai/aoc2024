import pytest

from app.day02.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            2,
        ),
    ],
)
def test_part_1(input_, expected):
    assert compute_part_1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            0,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
