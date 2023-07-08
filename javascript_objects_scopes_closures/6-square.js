#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let char = 'X';
    if (c) {
      char = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
