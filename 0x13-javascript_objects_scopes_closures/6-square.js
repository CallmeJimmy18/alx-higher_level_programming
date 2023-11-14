#!/usr/bin/node

const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      const wdthsq = c.repeat(this.width);
      console.log(wdthsq);
    }
  }
}

module.exports = Square;
