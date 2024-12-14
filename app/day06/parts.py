import sys
from enum import Enum

from app.support.utils import main, parse_module_to_day, timing


class GuardPosition(Enum):
    UP: str = "^"
    DOWN: str = "v"
    LEFT: str = "<"
    RIGHT: str = ">"


POSITIONS = (
    GuardPosition.UP.value,
    GuardPosition.DOWN.value,
    GuardPosition.LEFT.value,
    GuardPosition.RIGHT.value,
)


@timing
def compute_part_1(input_: str) -> int:
    matrix = list(list(c for c in line) for line in input_.splitlines())
    w, h = len(matrix[0]), len(matrix)
    guard_position = next(
        (rdx, idx, GuardPosition(c))
        for rdx, row in enumerate(matrix)
        for idx, c in enumerate(row)
        if c in POSITIONS
    )
    guard_in_map = True
    while guard_in_map:
        rdx, idx, direction = guard_position
        matrix[rdx][idx] = "X"  # Mark as visited

        boundaries: bool = (
            0 <= rdx + 1 < h
            and 0 <= idx + 1 < w
            and 0 <= rdx - 1 < h
            and 0 <= idx - 1 < w
        )

        match direction:
            case GuardPosition.UP:
                if boundaries and matrix[rdx - 1][idx] != "#":
                    rdx -= 1
                else:
                    direction = GuardPosition.RIGHT
            case GuardPosition.DOWN:
                if boundaries and matrix[rdx + 1][idx] != "#":
                    rdx += 1
                else:
                    direction = GuardPosition.LEFT
            case GuardPosition.LEFT:
                if boundaries and matrix[rdx][idx - 1] != "#":
                    idx -= 1
                else:
                    direction = GuardPosition.UP
            case GuardPosition.RIGHT:
                if boundaries and matrix[rdx][idx + 1] != "#":
                    idx += 1
                else:
                    direction = GuardPosition.DOWN

        guard_position = (rdx, idx, direction)
        if not boundaries:
            guard_in_map = False

    return sum(1 for row in matrix for c in row if c == "X")


@timing
def compute_part_2(s: str) -> int:
    if not s or not isinstance(s, str):
        return 0
    # Calculate response
    return 0


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
