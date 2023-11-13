#!/usr/bin/node

const arg = process.argv.slice(2);
const x = arg[0];
let i;

if (!x) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
