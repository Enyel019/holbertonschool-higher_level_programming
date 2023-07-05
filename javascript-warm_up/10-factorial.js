#!/usr/bin/node
const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
};
const number = parseInt(process.argv[2]);
console.log(`${factorial(number)}`);
