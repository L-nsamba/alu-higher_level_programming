#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2]; // first argument → file path
const content = process.argv[3]; // second argument → string to write

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
