#!/usr/bin/node

const SquareParent = require('./5-square.js');

class Square extends SquareParent {
  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
