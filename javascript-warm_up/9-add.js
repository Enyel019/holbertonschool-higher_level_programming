#!/usr/bin/node
const add = (a, b) => parseInt(a) + parseInt(b);

const firstNumber = process.argv[2];
const secondNumber = process.argv[3];

console.log(add(firstNumber, secondNumber));
