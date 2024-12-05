import sys
from collections import defaultdict

from app.support.utils import main, parse_module_to_day, timing


def parsing(input_: str) -> tuple[defaultdict[int, list[int]], tuple[tuple[int, ...] | None, ...]]:
    page_ordering_rules_raw, updates_raw = input_.split("\n\n")

    page_ordering_rules = tuple(
        map(
            lambda order: tuple(map(int, order.split("|"))),
            page_ordering_rules_raw.split("\n"),
        )
    )
    page_ordering_rules_dict = defaultdict(list)
    for order in page_ordering_rules:
        page_ordering_rules_dict[order[0]].append(order[1])

    updates_parsed = tuple(
        map(
            lambda update: tuple(map(int, update.split(","))) if update else None,
            filter(
                None,
                updates_raw.split("\n"),
            ),
        ),
    )

    return page_ordering_rules_dict, updates_parsed


@timing
def compute_part_1(input_: str) -> int:
    page_ordering_rules_dict, updates_parsed = parsing(input_)
    return sum(
        updates[(len(updates) - 1) // 2]
        for updates in updates_parsed
        if all(all(n in page_ordering_rules_dict[item] for n in updates[idx + 1 :]) for idx, item in enumerate(updates))
    )


@timing
def compute_part_2(input_: str) -> int:
    page_ordering_rules_dict, updates_parsed = parsing(input_)

    incorrectly_ordered_updates = {
        updates
        for updates in updates_parsed
        for idx, item in enumerate(updates)
        if not all(n in page_ordering_rules_dict[item] for n in updates[idx + 1 :])
    }

    return 0


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
