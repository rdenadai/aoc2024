const { readFile, strToInt } = require("../support/utils");

const computeDiff = (reports) =>
  reports.filter((report, idx) => {
    const nextReport = reports[idx < reports.length - 1 ? idx + 1 : idx];
    return nextReport < report
      ? report - nextReport <= 3
      : nextReport - report <= 3;
  }).length == reports.length;

const isIncreasing = (reports) =>
  !reports
    .map((report, idx) =>
      idx < reports.length - 1 ? report > reports[idx + 1] : true
    )
    .includes(false);

const isDecreasing = (reports) =>
  !reports
    .map((report, idx) =>
      idx < reports.length - 1 ? report < reports[idx + 1] : true
    )
    .includes(false);

const isSafe = (reports) =>
  computeDiff(reports) && (isIncreasing(reports) || isDecreasing(reports));

const compute_part_1 = () =>
  readFile("day02/input.txt")
    .split("\n")
    .map((line) => (line ? isSafe(line.split(/[\s]+/).map(strToInt)) : false))
    .reduce((acc, val) => (val ? acc + 1 : acc), 0);

const compute_part_2 = () =>
  readFile("day02/input.txt")
    .split("\n")
    .map((line) => {
      if (line) {
        const reports = line.split(/[\s]+/).map(strToInt);
        if (isSafe(reports)) {
          return true;
        } else {
          for (let index = 0; index <= reports.length; index++) {
            if (
              isSafe(reports.slice(0, index).concat(reports.slice(index + 1)))
            ) {
              return true;
            }
          }
        }
      }
      return false;
    })
    .reduce((acc, val) => (val ? acc + 1 : acc), 0);

console.assert(compute_part_1() == 341);
console.assert(compute_part_2() == 404);
