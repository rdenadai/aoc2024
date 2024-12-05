import pytest

from app.day04.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            18,
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
            9,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
