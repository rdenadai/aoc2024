import pytest

from app.day06.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

INPUT_TEXT_2 = """\
...#......
.......#..
..........
..#...<...
.......#..
..........
.#........
........#.
..........
......#...
"""

INPUT_TEXT_3 = """\
..........
.......#..
..........
..#...<...
.......#..
..........
.#........
........#.
..........
......#...
"""

INPUT_TEXT_4 = """\
..........
.......#..
..........
..#...>...
.......#..
..........
.#........
........#.
..........
......#...
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            41,
        ),
        (
            INPUT_TEXT_2,
            21,
        ),
        (
            INPUT_TEXT_3,
            7,
        ),
        (
            INPUT_TEXT_4,
            4,
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
            6,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected