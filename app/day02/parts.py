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


def is_safe(reports):
    return compute_diff(reports) and (is_increasing(reports) or is_decreasing(reports))


def compute_part_1(input_: str) -> int:
    return sum(is_safe(array("i", map(int, line.split()))) for line in input_.splitlines())


def compute_part_2(input_: str) -> int:
    amout_of_safe = 0
    for line in input_.splitlines():
        reports = array("i", map(int, line.split()))
        if is_safe(reports):
            amout_of_safe += 1
        else:
            for idx in range(0, len(reports)):
                if is_safe(reports[:idx] + reports[idx + 1 :]):
                    amout_of_safe += 1
                    break
    return amout_of_safe


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
