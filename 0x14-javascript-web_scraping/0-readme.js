#!/usr/bin/node

const fs = require('fs');
const flePath = process.argv[2];

fs.readFile(flePath, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
