const { readFile, strToInt } = require("../support/utils");

const PATTERN = [
  ["X", "M", "A", "S"],
  ["S", "A", "M", "X"],
];

const PATTERN_2 = [
  ["M", "A", "S"],
  ["S", "A", "M"],
];

const includes = (array, pattern) =>
  pattern.some((arr) =>
    arr.every((element, index) => element === array[index])
  );

const compute_part_1 = () => {
  let amount = 0;

  const matrix = readFile("day04/input2.txt")
    .split("\n")
    .map((line) => line.split(""));

  const [w, h] = [matrix[0].length, matrix.length];
  for (let ridx = 0; ridx < matrix.length; ridx++) {
    let max_h = ridx + 3 < h;
    for (let idx = 0; idx < matrix[ridx].length; idx++) {
      const c = matrix[ridx][idx];
      if (idx + 3 < w && includes(matrix[ridx].slice(idx, idx + 4), PATTERN)) {
        amount++;
      }
      if (
        max_h &&
        includes(
          [
            matrix[ridx][idx],
            matrix[ridx + 1][idx],
            matrix[ridx + 2][idx],
            matrix[ridx + 3][idx],
          ],
          PATTERN
        )
      ) {
        amount++;
      }
      if (
        idx + 3 < w &&
        max_h &&
        includes(
          [
            c,
            matrix[ridx + 1][idx + 1],
            matrix[ridx + 2][idx + 2],
            matrix[ridx + 3][idx + 3],
          ],
          PATTERN
        )
      ) {
        amount += 1;
      }
      if (
        idx >= 3 &&
        max_h &&
        includes(
          [
            c,
            matrix[ridx + 1][idx - 1],
            matrix[ridx + 2][idx - 2],
            matrix[ridx + 3][idx - 3],
          ],
          PATTERN
        )
      ) {
        amount += 1;
      }
    }
  }
  return amount;
};

const compute_part_2 = () => {
  let amount = 0;

  const matrix = readFile("day04/input2.txt")
    .split("\n")
    .map((line) => line.split(""));

  const [w, h] = [matrix[0].length, matrix.length];
  for (let ridx = 0; ridx < matrix.length; ridx++) {
    let max_h = ridx + 3 < h;
    for (let idx = 0; idx < matrix[ridx].length; idx++) {
      const c = matrix[ridx][idx];
      if (
        max_h &&
        idx + 2 < w &&
        includes(
          [c, matrix[ridx + 1][idx + 1], matrix[ridx + 2][idx + 2]],
          PATTERN_2
        ) &&
        includes(
          [
            matrix[ridx][idx + 2],
            matrix[ridx + 1][idx + 1],
            matrix[ridx + 2][idx],
          ],
          PATTERN_2
        )
      ) {
        amount += 1;
      }
    }
  }
  return amount;
};

console.assert(compute_part_1() == 18);
console.assert(compute_part_2() == 9);
