#!/usr/bin/node
const inputNumber = parseInt(process.argv[2], 10)
if (isNaN(inputNumber)) {
  console.log('Not a number')
} else {
  console.log(`My number: ${inputNumber}`)
}
