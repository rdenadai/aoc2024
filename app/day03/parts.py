import re
import sys
from enum import Enum

from app.support.utils import main, parse_module_to_day, timing

REGEX = r = re.compile(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))")


class Operation(Enum):
    MUL = "mul"
    DO = "do"
    DONT = "don't"


@timing
def compute_part_1(input_: str) -> int:
    return sum(int(n1) * int(n2) for op, n1, n2 in REGEX.findall(input_) if "mul" in op)


@timing
def compute_part_2(input_: str) -> int:
    execute = True
    instructions_sum = 0
    for idx, (op, n1, n2) in enumerate(REGEX.findall(input_)):
        match Operation(op.split("(")[0]):
            case Operation.MUL:
                if execute or idx == 0:
                    instructions_sum += int(n1) * int(n2)
            case Operation.DO:
                execute = True
            case Operation.DONT:
                execute = False
    return instructions_sum


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
