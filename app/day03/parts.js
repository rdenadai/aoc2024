const { readFile, strToInt } = require("../support/utils");

const REGEX = new RegExp(/(mul\((\d+),(\d+)\)|do\(\)|don't\(\))/g);

const compute_part_1 = () =>
  readFile("day03/input.txt")
    .matchAll(REGEX)
    .reduce((acc, item) => {
      const [_, op, n1, n2] = item;
      return op.includes("mul") ? acc + n1 * n2 : acc;
    }, 0);

const compute_part_2 = () => {
  let execute = true;
  let instructionsSum = 0;
  const items = readFile("day03/input.txt").matchAll(REGEX);
  items.forEach((item, idx) => {
    const [_, op, n1, n2] = item;
    if (op.includes("mul")) {
      instructionsSum += execute || idx == 0 ? strToInt(n1) * strToInt(n2) : 0;
    } else if (op.includes("don't")) {
      execute = false;
    } else {
      execute = true;
    }
  });
  return instructionsSum;
};

console.assert(compute_part_1() == 159833790);
console.assert(compute_part_2() == 89349241);
