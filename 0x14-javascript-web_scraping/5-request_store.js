#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const filePath = process.argv[3];
const url = process.argv[2];

request.get(url, 'utf-8', (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
