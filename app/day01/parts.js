const { readFile, strToInt } = require("../support/utils");

const compute_1 = () => {
  const num_left = [];
  const num_right = [];
  readFile("day01/input.txt")
    .split("\n")
    .forEach((line) => {
      const [left, right] = line.split(/[\s]+/);
      num_left.push(strToInt(left));
      num_right.push(strToInt(right));
    });
  num_left.sort((a, b) => a - b);
  num_right.sort((a, b) => a - b);

  return num_left
    .map((num, i) => Math.abs(num - num_right[i]))
    .reduce((acc, cur) => acc + cur, 0);
};

const compute_2 = () => {
  const num_left = [];
  const num_right = [];
  readFile("day01/input.txt")
    .split("\n")
    .forEach((line) => {
      const [left, right] = line.split(/[\s]+/);
      num_left.push(strToInt(left));
      num_right.push(strToInt(right));
    });

  return num_left
    .map((num, i) => num * num_right.filter((x) => x == num).length)
    .reduce((acc, cur) => acc + cur, 0);
};

console.assert(compute_1() == 1590491);
console.assert(compute_2() == 22588371);
