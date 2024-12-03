import sys
from array import array

from app.support.utils import main, parse_module_to_day


def compute_diff(reports):
    return all(
        (
            (
                report - next_report <= 3
                if (next_report := reports[idx + 1 if idx < len(reports) - 1 else idx]) < report
                else next_report - report <= 3
            )
            for idx, report in enumerate(reports)
        ),
    )


def is_increasing(reports):
    return all(report > reports[idx + 1] for idx, report in enumerate(reports) if idx < len(reports) - 1)


def is_decreasing(reports):
    return all(report < reports[idx + 1] for idx, report in enumerate(reports) if idx < len(reports) - 1)


def compute_part_1(input_: str) -> int:
    safe = []
    for line in input_.splitlines():
        reports = array("i", list(map(int, line.split())))
        safe.append(compute_diff(reports) and (is_increasing(reports) or is_decreasing(reports)))
    return sum(safe)


def compute_part_2(s: str) -> int:
    if not s or not isinstance(s, str):
        return 0
    # Calculate response
    return 0


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
