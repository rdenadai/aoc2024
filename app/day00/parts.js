const { readFile, strToInt } = require("../support/utils");

const compute_part_1 = () =>
  readFile("day00/input.txt")
    .split("\n")
    .map((line) => !!line)
    .reduce((acc, val) => (val ? acc + 1 : acc), 0);

const compute_part_2 = () =>
  readFile("day00/input.txt")
    .split("\n")
    .map((line) => !!line)
    .reduce((acc, val) => (val ? acc + 1 : acc), 0);

console.assert(compute_part_1() == 0);
console.assert(compute_part_2() == 0);
