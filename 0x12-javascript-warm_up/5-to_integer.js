#!/usr/bin/node

const arg = process.argv.slice(2);
const intVal = parseInt(arg[0]);

if (!isNaN(intVal)) {
  console.log('My number: ' + intVal);
} else {
  console.log('Not a number');
}
