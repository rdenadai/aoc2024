import sys

from app.support.utils import main, parse_module_to_day, timing

PATTERN = (("X", "M", "A", "S"), ("S", "A", "M", "X"))
PATTERN_2 = (("M", "A", "S"), ("S", "A", "M"))


@timing
def compute_part_1(input_: str) -> int:
    amount = 0

    matrix = tuple(tuple(c for c in line) for line in input_.splitlines())
    w, h = len(matrix[0]), len(matrix)
    for ridx, row in enumerate(matrix):
        max_h = ridx + 3 < h
        for idx, c in enumerate(row):
            if idx + 3 < w and row[idx : idx + 4] in PATTERN:
                amount += 1
            if (
                max_h
                and (
                    c,
                    matrix[ridx + 1][idx],
                    matrix[ridx + 2][idx],
                    matrix[ridx + 3][idx],
                )
                in PATTERN
            ):
                amount += 1
            if (
                idx + 3 < w
                and max_h
                and (
                    (
                        c,
                        matrix[ridx + 1][idx + 1],
                        matrix[ridx + 2][idx + 2],
                        matrix[ridx + 3][idx + 3],
                    )
                    in PATTERN
                )
            ):
                amount += 1
            if (
                idx >= 3
                and max_h
                and (
                    c,
                    matrix[ridx + 1][idx - 1],
                    matrix[ridx + 2][idx - 2],
                    matrix[ridx + 3][idx - 3],
                )
                in PATTERN
            ):
                amount += 1
    return amount


@timing
def compute_part_2(input_: str) -> int:
    amount = 0

    matrix = tuple(tuple(c for c in line) for line in input_.splitlines())
    w, h = len(matrix[0]), len(matrix)
    for ridx, row in enumerate(matrix):
        max_h = ridx + 2 < h
        for idx, c in enumerate(row):
            if (
                max_h
                and idx + 2 < w
                and (
                    (
                        c,
                        matrix[ridx + 1][idx + 1],
                        matrix[ridx + 2][idx + 2],
                    )
                    in PATTERN_2
                )
                and (
                    (
                        matrix[ridx][idx + 2],
                        matrix[ridx + 1][idx + 1],
                        matrix[ridx + 2][idx],
                    )
                    in PATTERN_2
                )
            ):
                amount += 1
    return amount


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
