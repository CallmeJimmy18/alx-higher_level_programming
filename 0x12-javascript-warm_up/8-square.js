#!/usr/bin/node

const args = process.argv.slice(2);
const arg = args[0];
let i;

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (i = 0; i < arg; i++) {
    const theXs = 'X'.repeat(arg);
    console.log(theXs);
  }
}
