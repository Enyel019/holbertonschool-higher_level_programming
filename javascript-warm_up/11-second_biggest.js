#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
const secondLargest = args.sort((a, b) => b - a)[1] || 0;
console.log(secondLargest);
