import sys
from array import array

from app.support.utils import main, parse_module_to_day, timing


def _compute(input_: str) -> list[int]:
    num_left, num_right = array("i"), array("i")
    for line in input_.splitlines():
        left, right = line.split()
        num_left.append(int(left))
        num_right.append(int(right))
    return [abs(l - r) for l, r in zip(sorted(num_left.tolist()), sorted(num_right.tolist()))]


def _compute_2(input_: str) -> list[int]:
    num_left, num_right = array("i"), array("i")
    for line in input_.splitlines():
        left, right = line.split()
        num_left.append(int(left))
        num_right.append(int(right))
    return [l * num_right.count(l) for l in sorted(num_left.tolist())]


@timing
def compute_part_1(input_: str) -> int:
    numbers: list[int] = _compute(input_)
    return sum(numbers)


@timing
def compute_part_2(input_: str) -> int:
    numbers: list[int] = _compute_2(input_)
    return sum(numbers)


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
