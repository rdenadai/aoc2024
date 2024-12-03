import pytest
from app.day01.parts import compute_part_1, compute_part_2

INPUT_TXT = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TXT,
            11,
        )
    ],
)
def test_part_1(input_, expected):
    assert compute_part_1(input_) == expected


INPUT_TXT_2 = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TXT_2,
            31,
        )
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
