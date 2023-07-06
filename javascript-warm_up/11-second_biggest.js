#!/usr/bin/node
const i = process.argv.slice(2);
if (process.argv.slice(2).length === 0) {
  console.log('0');
} else if (process.argv.slice(2).length === 1) {
  console.log('0');
}
if (process.argv.slice(2).length > 1) {
  const s = i.sort().length;
  console.log(i[s - 2]);
}
