#!/usr/bin/node
let i = parseInt(process.argv.slice(2)[0]);
if (isNaN(i)) {
  i = 1;
}
const factorial = factfun(i);
function factfun (n) {
  if (n < 0) {
    return;
  }
  if (n === 0) {
    return 1;
  }
  return n * factfun(n - 1);
}
console.log(factorial);
