import pytest

from app.day05.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            143,
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
