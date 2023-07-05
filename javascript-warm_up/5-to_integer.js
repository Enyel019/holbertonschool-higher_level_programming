#!/usr/bin/node
if (parseInt(process.argv.slice(2)[0])) {
  console.log('My number: %i', parseInt(process.argv.slice(2)[0]))
} else {
  console.log('Not a number')
}
