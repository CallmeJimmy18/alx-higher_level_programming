#!/usr/bin/node

const args = process.argv.slice(2);

function add (a, b) {
  const added = Number(a) + Number(b);
  console.log(added);
}

if (args.length < 2) {
  console.log('NaN');
} else {
  add(args[0], args[1]);
}
