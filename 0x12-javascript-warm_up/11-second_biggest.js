#!/usr/bin/node

const args = process.argv.slice(2);
let secLarge;

if (!args[0] || args.length === 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  secLarge = args[1];
  console.log(secLarge);
}
