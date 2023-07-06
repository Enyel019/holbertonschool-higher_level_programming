#!/usr/bin/node
const argsCount = process.argv.length - 2;
if (argsCount === 0) {
  console.log('0');
} else if (argsCount === 1) {
  console.log('0');
} else {
  console.log(argsCount - 2);
}
